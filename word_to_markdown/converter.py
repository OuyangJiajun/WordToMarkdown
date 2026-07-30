"""Core conversion logic for Word documents."""

from __future__ import annotations

import re
from pathlib import Path

import mammoth
from markdownify import markdownify as html_to_markdown

SUPPORTED_EXTENSIONS = {".docx", ".doc"}


class ConversionError(Exception):
    """Raised when a document cannot be converted."""


def convert_to_markdown(
    source: Path | str,
    *,
    images_dir: Path | str | None = None,
    use_pandoc: bool = True,
) -> str:
    """Convert a Word document to Markdown text.

    Args:
        source: Path to .docx or .doc file.
        images_dir: Directory to save extracted images. If None, images are omitted.
        use_pandoc: Prefer pandoc when available (recommended for .doc files).

    Returns:
        Markdown string.
    """
    source_path = Path(source).resolve()
    if not source_path.is_file():
        raise ConversionError(f"文件不存在: {source_path}")

    suffix = source_path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise ConversionError(
            f"不支持的文件格式: {suffix}，仅支持 {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
        )

    if use_pandoc and _pandoc_available():
        return _convert_with_pandoc(source_path)

    if suffix == ".doc":
        raise ConversionError(
            "旧版 .doc 格式需要安装 Pandoc。"
            "请从 https://pandoc.org/installing.html 安装后重试。"
        )

    return _convert_docx_with_mammoth(source_path, images_dir)


def convert_file(
    source: Path | str,
    output: Path | str | None = None,
    *,
    images_dir: Path | str | None = None,
    use_pandoc: bool = True,
) -> Path:
    """Convert a Word document and write Markdown to disk.

    Args:
        source: Input .docx/.doc path.
        output: Output .md path. Defaults to same name with .md extension.
        images_dir: Directory for extracted images. Defaults to ``<output_stem>_assets``.
        use_pandoc: Prefer pandoc when available.

    Returns:
        Path to the written Markdown file.
    """
    source_path = Path(source).resolve()
    output_path = Path(output).resolve() if output else source_path.with_suffix(".md")

    if images_dir is None:
        images_dir = output_path.parent / f"{output_path.stem}_assets"
    else:
        images_dir = Path(images_dir).resolve()

    markdown = convert_to_markdown(
        source_path,
        images_dir=images_dir,
        use_pandoc=use_pandoc,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    return output_path


def _pandoc_available() -> bool:
    try:
        import pypandoc

        return pypandoc.get_pandoc_path() is not None
    except (ImportError, OSError, RuntimeError):
        return False


def _convert_with_pandoc(source_path: Path) -> str:
    import pypandoc

    try:
        return pypandoc.convert_file(
            str(source_path),
            "markdown",
            format="docx" if source_path.suffix.lower() == ".docx" else "doc",
            extra_args=["--wrap=none", "--markdown-headings=atx"],
        )
    except RuntimeError as exc:
        raise ConversionError(f"Pandoc 转换失败: {exc}") from exc


def _convert_docx_with_mammoth(
    source_path: Path,
    images_dir: Path | str | None,
) -> str:
    images_path = Path(images_dir).resolve() if images_dir else None
    if images_path:
        images_path.mkdir(parents=True, exist_ok=True)

    image_counter = 0

    def convert_image(image) -> dict[str, str]:
        nonlocal image_counter
        if images_path is None:
            return {"src": ""}

        image_counter += 1
        ext = _guess_image_extension(image.content_type)
        filename = f"image_{image_counter:03d}{ext}"
        with image.open() as image_bytes:
            (images_path / filename).write_bytes(image_bytes.read())
        return {"src": f"{images_path.name}/{filename}"}

    try:
        with source_path.open("rb") as docx_file:
            result = mammoth.convert_to_html(
                docx_file,
                convert_image=mammoth.images.img_element(convert_image),
            )
    except Exception as exc:
        raise ConversionError(f"读取 Word 文档失败: {exc}") from exc

    for message in result.messages:
        if message.type == "error":
            raise ConversionError(f"文档解析错误: {message.message}")

    markdown = html_to_markdown(
        result.value,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )
    return _clean_markdown(markdown)


def _guess_image_extension(content_type: str) -> str:
    mapping = {
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/gif": ".gif",
        "image/bmp": ".bmp",
        "image/webp": ".webp",
        "image/tiff": ".tiff",
    }
    return mapping.get(content_type, ".png")


def _clean_markdown(text: str) -> str:
    """Normalize whitespace and fix common conversion artifacts."""
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip() + "\n"
