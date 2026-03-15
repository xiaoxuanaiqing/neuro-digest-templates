# Word 文档排版规范

## 📄 页面设置

| 参数 | 值 |
|------|-----|
| 纸张大小 | A4 |
| 上边距 | 2.5cm |
| 下边距 | 2.5cm |
| 左边距 | 3cm |
| 右边距 | 3cm |
| 页眉 | 1.5cm (可选) |
| 页脚 | 1.5cm (可选) |

## 🎨 配色方案

| 用途 | 颜色代码 | 说明 |
|------|----------|------|
| 主标题 | `#1a365d` | 深蓝 |
| 副标题 | `#2c5282` | 中蓝 |
| 正文 | `#2d3748` | 深灰 |
| 注释 | `#718096` | 中灰 |
| 强调 | `#c53030` | 深红 (可选) |

## 🔤 字体规范

### 标题页
- **主标题**: Microsoft YaHei Bold, 22pt, 居中, `#1a365d`
- **日期**: Microsoft YaHei Regular, 14pt, 居中, `#718096`
- **副标题**: Microsoft YaHei Regular, 12pt, 居中, `#718096`

### 文章条目

#### 1. 序号与英文标题
- **格式**: Bold, 14pt, `#1a365d`
- **示例**: `1. Astrocytic Mitochondria Transplantation...`
- **段前**: 12pt
- **段后**: 6pt

#### 2. 中文翻译
- **格式**: Italic, 12pt, `#4a5568`
- **示例**: `*星形胶质细胞线粒体移植...*`
- **段前**: 0pt
- **段后**: 6pt

#### 3. 摘要正文
- **格式**: Regular, 11pt, `#2d3748`
- **行距**: 1.5倍
- **首行缩进**: 0cm (顶格)
- **段前**: 0pt
- **段后**: 6pt

#### 4. 来源信息
- **格式**: Italic, 10pt, `#718096`
- **示例**: `📄 Annals of Neurology | 2026-03-12`
- **段前**: 0pt
- **段后**: 12pt

## 📏 段落格式

| 元素 | 段前 | 段后 | 行距 |
|------|------|------|------|
| 分隔线 | - | 6pt | - |
| 文章标题 | 12pt | 6pt | 单倍 |
| 中文翻译 | 0pt | 6pt | 单倍 |
| 摘要 | 0pt | 6pt | 1.5倍 |
| 来源 | 0pt | 12pt | 单倍 |
| 分隔线(后) | 6pt | - | - |

## 📊 特殊元素

### 分隔线
- 使用细线分隔不同文章
- 颜色: `#e2e8f0` (浅灰)
- 宽度: 100%

### 统计信息
- 位置: 文档末尾
- 格式: 灰色背景文本框 (可选)
- 内容: 总文章数、来源期刊分布

## 💡 排版技巧

1. **保持简洁**: 避免过多装饰元素
2. **层次分明**: 通过字号和颜色区分层级
3. **留白充足**: 段间距适当，不要拥挤
4. **对齐统一**: 左对齐为主，标题可居中
5. **字体嵌入**: 导出时嵌入字体，避免兼容问题

## 🐍 Python 实现参考

```python
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

def set_style(run, font_name, font_size, bold=False, italic=False, color=None):
    """设置文本样式"""
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)

def add_article(doc, number, en_title, cn_title, abstract, journal, date):
    """添加一篇文章"""
    # 分隔线
    doc.add_paragraph().add_run().add_break()
    
    # 序号+英文标题
    p = doc.add_paragraph()
    run = p.add_run(f"{number}. {en_title}")
    set_style(run, 'Microsoft YaHei', 14, bold=True, color=(26, 54, 93))
    
    # 中文翻译
    p = doc.add_paragraph()
    run = p.add_run(cn_title)
    set_style(run, 'Microsoft YaHei', 12, italic=True, color=(74, 85, 104))
    
    # 摘要
    p = doc.add_paragraph()
    run = p.add_run(f"摘要：{abstract}")
    set_style(run, 'Microsoft YaHei', 11, color=(45, 55, 72))
    
    # 来源
    p = doc.add_paragraph()
    run = p.add_run(f"📄 {journal} | {date}")
    set_style(run, 'Microsoft YaHei', 10, italic=True, color=(113, 128, 150))
```

## ✅ 质量检查清单

- [ ] 字体大小符合规范
- [ ] 颜色使用正确
- [ ] 段落间距一致
- [ ] 中英文标题对应
- [ ] 摘要内容完整未删减
- [ ] 来源信息准确
- [ ] 页边距设置正确
- [ ] 整体风格简约高级
