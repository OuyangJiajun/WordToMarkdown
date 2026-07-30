# WordToMarkdown

将 Word 文档（`.docx` / `.doc`）转换为 Markdown 格式的命令行工具。

## 功能

- 支持 `.docx` 和 `.doc` 格式
- 自动提取文档中的图片到独立目录
- 支持单文件或批量（目录递归）转换
- 双引擎：优先使用 [Pandoc](https://pandoc.org/)（质量更高），回退到 [mammoth](https://github.com/mwilliamson/python-mammoth)（无需额外安装）

## 安装

### 1. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

或安装为可执行命令：

```bash
pip install -e .
```

### 2. （可选）安装 Pandoc

处理 `.doc` 旧格式或获得更高转换质量，建议安装 Pandoc：

- Windows: https://pandoc.org/installing.html
- macOS: `brew install pandoc`
- Linux: `sudo apt install pandoc`

## 使用方法

### 命令行

```bash
# 转换单个文件（输出为 document.md）
python -m word_to_markdown document.docx

# 指定输出路径
python -m word_to_markdown document.docx -o output/readme.md

# 批量转换目录下所有 Word 文件
python -m word_to_markdown ./docs/

# 指定图片输出目录
python -m word_to_markdown report.docx --images-dir ./images

# 强制使用 mammoth 引擎（不依赖 Pandoc，仅 .docx）
python -m word_to_markdown report.docx --no-pandoc
```

安装后也可直接使用 `word2md` 命令：

```bash
word2md document.docx
```

### Python API

```python
from word_to_markdown import convert_file, convert_to_markdown

# 转换并保存文件
output_path = convert_file("document.docx")
print(f"已保存到: {output_path}")

# 仅获取 Markdown 文本
markdown_text = convert_to_markdown("document.docx")
print(markdown_text)
```

## 输出说明

- 默认输出文件与源文件同名，扩展名为 `.md`
- 图片默认保存到 `<输出文件名>_assets/` 目录
- Markdown 中使用 ATX 风格标题（`#`、`##` 等）

## 项目结构

```
WordToMarkdown/
├── word_to_markdown/
│   ├── __init__.py      # 包入口
│   ├── converter.py     # 核心转换逻辑
│   ├── cli.py           # 命令行接口
│   └── __main__.py      # python -m 入口
├── requirements.txt
├── pyproject.toml
└── README.md
```

## 依赖

| 包 | 用途 |
|---|---|
| [mammoth](https://github.com/mwilliamson/python-mammoth) | .docx → HTML 解析 |
| [markdownify](https://github.com/matthewwithanm/python-markdownify) | HTML → Markdown |
| [pypandoc](https://github.com/JessicaTegner/pypandoc) | Pandoc 封装（可选，需系统安装 pandoc） |

## License

MIT
