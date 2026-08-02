"""Core conversion logic for Word documents."""

from __future__ import annotations

import html as html_module
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
    reference_dir: Path | str | None = None,
) -> str:
    """Convert a Word document to Markdown text.

    Args:
        source: Path to .docx or .doc file.
        images_dir: Directory to save extracted images. If None, images are omitted.
        use_pandoc: Prefer pandoc when available (recommended for .doc files).
        reference_dir: Directory containing the generated Markdown file.

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
        return _convert_with_pandoc(source_path, images_dir)

    if suffix == ".doc":
        raise ConversionError(
            "旧版 .doc 格式需要安装 Pandoc。"
            "请从 https://pandoc.org/installing.html 安装后重试。"
        )

    return _convert_docx_with_mammoth(source_path, images_dir, reference_dir)


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

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise ConversionError(f"创建输出目录失败: {output_path.parent}: {exc}") from exc

    markdown = convert_to_markdown(
        source_path,
        images_dir=images_dir,
        use_pandoc=use_pandoc,
        reference_dir=output_path.parent,
    )

    try:
        output_path.write_text(markdown, encoding="utf-8")
    except OSError as exc:
        raise ConversionError(f"写入 Markdown 文件失败: {output_path}: {exc}") from exc
    return output_path


def _pandoc_available() -> bool:
    try:
        import pypandoc

        return pypandoc.get_pandoc_path() is not None
    except (ImportError, OSError, RuntimeError):
        return False


def _convert_with_pandoc(
    source_path: Path,
    images_dir: Path | str | None,
) -> str:
    import pypandoc

    extra_args = ["--wrap=none", "--markdown-headings=atx"]
    if images_dir is not None:
        images_path = Path(images_dir).resolve()
        try:
            images_path.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            raise ConversionError(f"创建图片目录失败: {images_path}: {exc}") from exc
        extra_args.append(f"--extract-media={images_path}")

    try:
        return pypandoc.convert_file(
            str(source_path),
            "markdown",
            format="docx" if source_path.suffix.lower() == ".docx" else "doc",
            extra_args=extra_args,
        )
    except RuntimeError as exc:
        raise ConversionError(f"Pandoc 转换失败: {exc}") from exc


def _convert_docx_with_mammoth(
    source_path: Path,
    images_dir: Path | str | None,
    reference_dir: Path | str | None,
) -> str:
    images_path = Path(images_dir).resolve() if images_dir else None
    reference_path = Path(reference_dir).resolve() if reference_dir else source_path.parent
    if images_path:
        try:
            images_path.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            raise ConversionError(f"创建图片目录失败: {images_path}: {exc}") from exc

    image_counter = 0
    image_code_map: dict[str, str] = {}

    def convert_image(image) -> dict[str, str]:
        nonlocal image_counter
        if images_path is None:
            return {"src": ""}

        image_counter += 1
        ext = _guess_image_extension(image.content_type)
        filename = f"image_{image_counter:03d}{ext}"
        image_path = images_path / filename
        try:
            with image.open() as image_bytes:
                image_path.write_bytes(image_bytes.read())
        except OSError as exc:
            raise ConversionError(f"保存图片失败: {image_path}: {exc}") from exc

        try:
            src = image_path.relative_to(reference_path).as_posix()
        except ValueError:
            src = image_path.as_uri()
        code_text = _extract_code_from_image(image_path)
        if code_text:
            image_code_map[src] = code_text

        return {"src": src}

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

    html = _replace_code_images(result.value, image_code_map)
    markdown = html_to_markdown(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )
    return _clean_markdown(markdown)


def _replace_code_images(html: str, image_code_map: dict[str, str]) -> str:
    if not image_code_map:
        return html

    def replace_match(match: re.Match[str]) -> str:
        tag = match.group(0)
        src_match = re.search(r'src=["\']([^"\']+)["\']', tag, flags=re.IGNORECASE)
        if not src_match:
            return tag
        src = html_module.unescape(src_match.group(1))
        code_text = image_code_map.get(src)
        if not code_text:
            return tag
        escaped = html_module.escape(code_text)
        return f"<pre><code>{escaped}</code></pre>"

    return re.sub(r"<img\b[^>]*>", replace_match, html, flags=re.IGNORECASE)


def _extract_code_from_image(image_path: Path) -> str | None:
    """Try to OCR an image and keep it when it looks like code.

    The OCR path is optional: if `pytesseract` or `Pillow` is unavailable,
    the image stays an image.
    """
    try:
        from PIL import Image  # type: ignore
        import pytesseract  # type: ignore
    except Exception:
        return None

    try:
        text = pytesseract.image_to_string(Image.open(image_path), lang="eng+chi_sim")
    except Exception:
        return None

    normalized = _clean_ocr_text(text)
    if not normalized:
        return None
    if _looks_like_code(normalized):
        return normalized
    return None


def _clean_ocr_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def _looks_like_code(text: str) -> bool:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return False

    code_tokens = sum(
        1
        for token in (";", "{", "}", "=", "(", ")", "[", "]", "<", ">", "::", "->", "#include")
        if token in text
    )
    keyword_hits = sum(
        1 for keyword in ("int ", "char ", "void ", "for ", "while ", "if ", "else", "return ") if keyword in text
    )
    indentation_hits = sum(1 for line in lines[1:] if line.startswith((" ", "\t")))

    return code_tokens >= 3 or keyword_hits >= 2 or indentation_hits >= 2


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
