# WordToMarkdown 项目架构说明

## 一、整体架构

项目采用分层架构，将启动入口、命令行适配、公共 API 和核心转换逻辑分开：

```text
用户
 │
 ├── 命令行方式
 │       │
 │       └── __main__.py
 │               │
 │               └── cli.py
 │                       │
 │                       └── converter.py
 │
 └── Python API 方式
         │
         └── __init__.py
                 │
                 └── converter.py
```

项目结构：

```text
WordToMarkdown/
├── word_to_markdown/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   └── converter.py
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

## 二、各模块职责

### `__init__.py`：公共 API 层

负责提供稳定、简洁的 Python API：

```python
from word_to_markdown import convert_file, convert_to_markdown
```

用户不需要了解具体实现位于哪个内部模块。这样可以在重构内部代码时尽量保持对外接口不变。

### `__main__.py`：模块启动入口

负责支持：

```bash
python -m word_to_markdown
```

它本身不包含业务逻辑，只将程序启动流程交给 `cli.main()`，符合“入口层尽量薄”的原则。

### `cli.py`：命令行适配层

负责：

- 解析命令行参数
- 收集输入文件
- 校验参数组合
- 调用 `convert_file()`
- 输出成功或失败信息
- 返回命令行退出码

命令行只是用户交互方式之一，因此不应将命令行逻辑混入核心转换模块。未来增加 Web API、GUI 或 Jupyter 使用方式时，可以直接复用核心转换逻辑。

### `converter.py`：核心业务层

负责：

- 验证输入文件
- 选择转换引擎
- 调用 Pandoc 或 Mammoth
- 提取图片
- 执行可选 OCR
- 将内容转换成 Markdown
- 清理 Markdown
- 将 Markdown 写入文件

核心流程：

```text
Word 文件
   │
   ├── 文件和格式校验
   │
   ├── 选择 Pandoc 或 Mammoth
   │
   ├── 转换为中间格式
   │
   ├── 提取图片
   │
   ├── 可选 OCR
   │
   ├── 转换为 Markdown
   │
   └── 清理 Markdown
```

## 三、为什么采用 Pandoc + Mammoth 双引擎

### Pandoc

Pandoc：

- 支持 `.docx`
- 支持旧版 `.doc`
- 对复杂文档通常有较好的转换能力
- 支持媒体文件提取

缺点是需要额外安装系统级 Pandoc。

### Mammoth

Mammoth：

- 适合处理 `.docx`
- Python 调用简单
- 支持自定义图片处理回调
- 便于接入 OCR

缺点是不能处理旧版 `.doc`。

### 双引擎的意义

双引擎提供了能力降级机制：

```text
Pandoc 可用
  ├── .doc  → Pandoc
  └── .docx → Pandoc

Pandoc 不可用
  └── .docx → Mammoth

Pandoc 不可用
  └── .doc  → 提示安装 Pandoc
```

有 Pandoc 时可以获得更好的格式兼容性；没有 Pandoc 时，用户仍然可以处理 `.docx`。

## 四、为什么采用 DOCX → HTML → Markdown

Mammoth 主要输出 HTML，项目再通过 `markdownify` 转换为 Markdown：

```text
DOCX → HTML → Markdown
```

HTML 作为中间格式有几个优点：

- 可以表达标题、段落、粗体、列表、表格、链接和图片
- 方便在转换阶段处理图片
- 可以使用成熟的 HTML 到 Markdown 转换库
- 避免自行实现复杂的格式转换规则

## 五、为什么区分 `convert_to_markdown()` 和 `convert_file()`

### `convert_to_markdown()`

负责转换并返回 Markdown 字符串：

```python
markdown = convert_to_markdown("document.docx")
```

适合：

- Web 服务
- 单元测试
- 在内存中继续处理
- 自定义输出逻辑
- Jupyter Notebook

### `convert_file()`

负责转换并将 Markdown 写入文件：

```python
output = convert_file("document.docx")
```

这种拆分遵循单一职责原则：

```text
convert_to_markdown：负责转换
convert_file：负责文件输出
```

## 六、为什么定义 `ConversionError`

项目使用统一的业务异常类型表示转换失败：

```python
class ConversionError(Exception):
    ...
```

底层可能产生文件不存在、权限错误、Pandoc 错误、Mammoth 解析错误等不同异常。统一包装为 `ConversionError` 后，CLI 只需要捕获一种异常：

```python
except ConversionError as exc:
    print(f"[FAIL] {source.name}: {exc}")
```

这样可以：

- 隔离底层第三方库细节
- 提供更友好的错误信息
- 方便 API 调用者统一处理错误
- 便于未来替换转换引擎

## 七、为什么使用图片处理回调

Mammoth 提供图片转换回调，项目可以在图片被转换为 HTML 时立即处理：

```text
Mammoth 发现图片
       ↓
保存图片
       ↓
生成图片路径
       ↓
执行 OCR
       ↓
返回 HTML 图片属性
```

这种方式可以直接获得图片的二进制内容和 MIME 类型，比转换完成后再扫描 HTML 更可靠，也便于扩展图片压缩、格式转换和去重功能。

## 八、当前架构的优点

1. **入口和业务逻辑分离**：`__main__.py`、`cli.py` 和 `converter.py` 职责清晰。
2. **同时支持 CLI 和 Python API**：不同使用场景可以复用同一套核心逻辑。
3. **具备降级策略**：Pandoc 不可用时，`.docx` 仍可通过 Mammoth 转换。
4. **图片处理具有扩展能力**：支持图片提取、自定义目录、路径处理和 OCR。
5. **对外 API 较稳定**：用户主要依赖 `convert_file()`、`convert_to_markdown()` 和 `ConversionError`，内部函数可以独立重构。

## 九、可以优化的地方

### 1. 抽象转换引擎

目前转换引擎选择逻辑直接写在 `converter.py` 中。随着引擎数量增加，条件分支会越来越多。

可以定义统一的转换引擎协议：

```python
class ConversionEngine(Protocol):
    def supports(self, source: Path) -> bool:
        ...

    def convert(self, source: Path, options: ConversionOptions) -> str:
        ...
```

然后实现：

```text
PandocEngine
MammothEngine
```

未来增加 LibreOffice、OnlyOffice 或云端转换服务时，不需要不断修改主流程。

### 2. 使用配置对象

当前参数数量可能继续增加，例如 OCR 开关、OCR 语言、图片命名规则和 Markdown 风格。可以使用配置对象集中管理：

```python
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ConversionOptions:
    images_dir: Path | None = None
    reference_dir: Path | None = None
    use_pandoc: bool = True
    enable_ocr: bool = True
```

优点是参数集中、扩展方便、配置可复用、测试更简单。

### 3. 拆分图片处理模块

当前 `converter.py` 同时负责文件验证、引擎选择、Pandoc、Mammoth、图片保存、OCR、HTML 替换和 Markdown 清理。项目继续扩展时，可以拆分为：

```text
word_to_markdown/
├── engines/
│   ├── pandoc.py
│   └── mammoth.py
├── media.py
├── ocr.py
└── markdown.py
```

建议职责：

- `engines/pandoc.py`：Pandoc 检测和转换
- `engines/mammoth.py`：Mammoth 转换和图片回调
- `media.py`：图片目录、命名、保存和相对路径
- `ocr.py`：OCR 和代码识别
- `markdown.py`：HTML 转 Markdown、代码图片替换和清理

### 4. 引入转换上下文

当前图片计数器、图片目录、引用目录和 OCR 映射关系分散在闭包和函数参数中。可以使用 `ConversionContext` 统一管理这些状态：

```python
@dataclass
class ConversionContext:
    images_dir: Path | None
    reference_dir: Path
    image_counter: int = 0
    image_code_map: dict[str, str] = field(default_factory=dict)
```

这样可以减少隐式状态，也方便单元测试和未来实现图片去重。

### 5. 统一 Pandoc 和 Mammoth 的媒体行为

目前 Pandoc 使用 `--extract-media`，Mammoth 使用自定义图片回调。两种引擎可能产生不同的目录结构、文件名和 Markdown 图片引用。

建议定义统一的媒体管理器：

```python
class MediaManager:
    def save(self, data: bytes, content_type: str) -> str:
        ...
```

目标是让不同转换引擎最终使用统一的图片目录、命名规则和引用路径。

### 6. 抽出批量转换服务

当前批量转换循环位于 `cli.py`。可以抽出可复用的服务函数：

```python
def convert_many(
    sources: Iterable[Path],
    *,
    images_dir: Path | None = None,
    use_pandoc: bool = True,
) -> list[ConversionResult]:
    ...
```

CLI 只负责解析参数和格式化结果。未来 GUI 或 Web 接口也可以直接复用批量转换服务。

## 十、建议的优化后架构

如果项目继续发展，可以采用：

```text
word_to_markdown/
├── __init__.py
├── __main__.py
├── cli.py
├── models.py
├── service.py
├── converter.py
├── engines/
│   ├── __init__.py
│   ├── base.py
│   ├── pandoc.py
│   └── mammoth.py
├── media.py
├── ocr.py
└── markdown.py
```

### `models.py`

定义转换配置和转换结果。

### `service.py`

提供单文件和批量转换服务。

### `engines/base.py`

定义转换引擎协议。

### `engines/pandoc.py` 和 `engines/mammoth.py`

分别实现具体转换引擎。

### `media.py`

统一管理图片保存、命名、路径和媒体目录。

### `ocr.py`

集中处理 OCR 依赖、文本提取和代码检测。

## 十一、是否应该立即拆分模块

不建议一次性进行大规模重构。当前项目规模较小，现有架构已经能够满足基本使用需求。

推荐按以下顺序渐进优化：

1. 增加自动化测试
2. 引入 `ConversionOptions`
3. 抽出图片管理器
4. 抽出批量转换服务
5. 统一 Pandoc 和 Mammoth 的媒体行为
6. 在功能继续增长后再拆分引擎、OCR 和 Markdown 模块

当出现以下情况时，再进行更彻底的模块拆分：

- `converter.py` 超过约 400～500 行
- OCR 逻辑继续扩展
- 增加第三种转换引擎
- 需要处理更多表格、样式和链接规则
- 多个开发者并行维护
- 各功能需要大量独立测试

## 十二、最终评价

当前架构的核心思想是正确的：

```text
稳定入口
  ↓
命令行适配
  ↓
统一转换 API
  ↓
可切换转换引擎
  ↓
图片和 Markdown 后处理
```

它适合当前项目，因为同时满足了 CLI 使用、Python API 使用、Pandoc 可选、Mammoth 降级、图片处理和 OCR 扩展等需求。

随着功能增加，`converter.py` 会逐渐承担过多职责。最值得进行的下一步优化是：

```text
配置对象
+ 转换引擎抽象
+ 独立媒体管理
+ 独立 OCR 模块
+ 批量转换服务
+ 自动化测试
```

如果项目只是个人工具，当前架构已经够用；如果目标是长期维护、发布到 PyPI 或作为团队基础库，则建议逐步演进为“服务层 + 引擎层 + 媒体处理层”的架构。
