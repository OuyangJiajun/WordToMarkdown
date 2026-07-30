"""Command-line interface."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from word_to_markdown.converter import ConversionError, SUPPORTED_EXTENSIONS, convert_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="word2md",
        description="将 Word 文档（.docx / .doc）转换为 Markdown 格式。",
    )
    parser.add_argument(
        "input",
        nargs="+",
        help="输入的 Word 文件或目录（目录会递归处理其中的 Word 文件）",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="输出 Markdown 文件路径（仅单文件输入时有效）",
    )
    parser.add_argument(
        "--images-dir",
        help="图片输出目录（默认: <输出文件名>_assets）",
    )
    parser.add_argument(
        "--no-pandoc",
        action="store_true",
        help="不使用 Pandoc，强制使用 mammoth 引擎（仅支持 .docx）",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="静默模式，不输出进度信息",
    )
    return parser


def collect_word_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        path = Path(raw).resolve()
        if path.is_file():
            if path.suffix.lower() in SUPPORTED_EXTENSIONS:
                files.append(path)
            else:
                print(f"跳过非 Word 文件: {path}", file=sys.stderr)
        elif path.is_dir():
            for ext in SUPPORTED_EXTENSIONS:
                files.extend(sorted(path.rglob(f"*{ext}")))
        else:
            print(f"路径不存在: {path}", file=sys.stderr)
    return files


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    word_files = collect_word_files(args.input)
    if not word_files:
        print("未找到可转换的 Word 文件。", file=sys.stderr)
        return 1

    if args.output and len(word_files) > 1:
        print("批量转换时不能指定 -o，请省略该参数。", file=sys.stderr)
        return 1

    use_pandoc = not args.no_pandoc
    failed = 0

    for source in word_files:
        output = Path(args.output).resolve() if args.output else None
        try:
            result = convert_file(
                source,
                output=output,
                images_dir=args.images_dir,
                use_pandoc=use_pandoc,
            )
            if not args.quiet:
                print(f"[OK] {source.name} -> {result}")
        except ConversionError as exc:
            failed += 1
            print(f"[FAIL] {source.name}: {exc}", file=sys.stderr)

    if failed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
