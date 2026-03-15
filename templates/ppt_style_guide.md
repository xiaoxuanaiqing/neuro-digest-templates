# PPT 演示文稿排版规范

## 🎨 整体设计

### 主题风格
- **风格**: 简约学术风
- **背景**: 纯白 (#ffffff)
- **主色调**: 深蓝 `#1a365d`
- **辅色调**: 中灰 `#718096`

### 页面尺寸
- **比例**: 16:9 (宽屏)
- **宽度**: 33.867 cm
- **高度**: 19.05 cm

## 📑 页面类型

### 1. 标题页 (Slide 1)

#### 布局
```
+------------------------------------------+
|                                          |
|                                          |
|         🧠 Neuroscience                  |
|         Daily Digest                     |
|                                          |
|         ----------------                 |
|                                          |
|         2026年3月12日                    |
|         星期三                           |
|                                          |
|         精选 10 篇文献                   |
|                                          |
+------------------------------------------+
```

#### 元素规范
| 元素 | 字体 | 大小 | 颜色 | 位置 |
|------|------|------|------|------|
| 图标 | Segoe UI Emoji | 48pt | `#1a365d` | 顶部居中 |
| 主标题 | Microsoft YaHei Bold | 36pt | `#1a365d` | 居中 |
| 副标题 | Microsoft YaHei Light | 24pt | `#2c5282` | 主标题下方 |
| 日期 | Microsoft YaHei | 18pt | `#718096` | 中下部 |
| 星期 | Microsoft YaHei | 14pt | `#a0aec0` | 日期下方 |
| 统计 | Microsoft YaHei | 16pt | `#4a5568` | 底部 |

### 2. 目录页 (Slide 2, 可选)

#### 布局
- 左侧: 标题 "今日精选"
- 右侧: 文章列表（仅英文标题，精简）

#### 元素规范
- **标题**: 28pt, Bold, `#1a365d`
- **列表项**: 14pt, Regular, `#2d3748`
- **行距**: 1.3倍

### 3. 内容页 (Slide 3+)

#### 布局选项

**选项 A: 单篇文章（详细版）**
```
+------------------------------------------+
| 1. Article Title (English)               |
|    *中文标题*                             |
|                                          |
| 摘要内容...                               |
| 摘要内容...                               |
| 摘要内容...                               |
|                                          |
| 📄 Journal Name | 2026-03-12             |
+------------------------------------------+
```

**选项 B: 两篇文章（精简版）**
```
+------------------------------------------+
| 1. Title One            2. Title Two     |
|    *中文一*                *中文二*       |
|                                          |
| 摘要一...               摘要二...        |
|                                          |
| 📄 Source 1             📄 Source 2      |
+------------------------------------------+
```

#### 元素规范

| 元素 | 字体 | 大小 | 颜色 | 其他 |
|------|------|------|------|------|
| 序号+英文标题 | Microsoft YaHei Bold | 20pt | `#1a365d` | 左对齐 |
| 中文标题 | Microsoft YaHei | 16pt | `#4a5568` | Italic |
| 摘要 | Microsoft YaHei | 14pt | `#2d3748` | 行距1.3 |
| 来源 | Microsoft YaHei | 12pt | `#718096` | Italic, 底部 |

### 4. 结束页 (最后一页)

#### 布局
- 居中显示 "Thank You" 或 "谢谢阅读"
- 底部可添加联系方式或二维码（可选）

#### 元素规范
- **主文字**: 32pt, Bold, `#1a365d`
- **副文字**: 18pt, Regular, `#718096`

## 🎨 配色方案

### 主色板
```
深蓝:   #1a365d  (标题、强调)
中蓝:   #2c5282  (副标题)
浅蓝:   #4299e1  (链接、可选强调)
```

### 中性色
```
深灰:   #2d3748  (正文)
中灰:   #4a5568  (次要文字)
浅灰:   #718096  (注释、来源)
极浅灰: #a0aec0  (装饰)
```

### 背景色
```
纯白:   #ffffff  (主背景)
浅灰底: #f7fafc  (可选卡片背景)
```

## 📐 间距规范

### 页面边距
- 上: 2cm
- 下: 2cm
- 左: 2.5cm
- 右: 2.5cm

### 元素间距
| 场景 | 间距 |
|------|------|
| 标题与副标题 | 0.5cm |
| 副标题与内容 | 1cm |
| 段落之间 | 0.8cm |
| 文章之间 | 1.2cm |

## 🖼️ 图形元素

### 分隔线
- 使用细线分隔不同文章
- 颜色: `#e2e8f0`
- 粗细: 1pt
- 长度: 100% 或 80% (居中)

### 图标
- 来源: Fluent UI 或 Segoe UI Emoji
- 大小: 与文字协调
- 常用: 🧠 📄 🔬 📊

### 形状 (可选)
- 标题左侧可加竖条装饰
- 颜色: `#1a365d`
- 宽度: 4pt
- 高度: 与标题行高相同

## 💡 排版技巧

1. **一致性**: 每页结构保持一致
2. **留白**: 不要填满，保持呼吸感
3. **对比**: 标题与正文大小对比明显
4. **对齐**: 严格左对齐，保持整洁
5. **精简**: 每页不超过2篇文章
6. **分页**: 长摘要适当分页

## 🐍 Python 实现参考

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def set_text_style(text_frame, font_name, font_size, bold=False, color=None):
    """设置文本框样式"""
    for paragraph in text_frame.paragraphs:
        paragraph.alignment = PP_ALIGN.LEFT
        for run in paragraph.runs:
            run.font.name = font_name
            run.font.size = Pt(font_size)
            run.font.bold = bold
            if color:
                run.font.color.rgb = RGBColor(*color)

def create_title_slide(prs, date_str, count):
    """创建标题页"""
    slide_layout = prs.slide_layouts[6]  # 空白布局
    slide = prs.slides.add_slide(slide_layout)
    
    # 添加标题
    title_box = slide.shapes.add_textbox(
        Inches(1), Inches(2.5), Inches(8), Inches(1.5)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "🧠 Neuroscience"
    p.alignment = PP_ALIGN.CENTER
    set_text_style(tf, 'Microsoft YaHei', 36, bold=True, color=(26, 54, 93))
    
    # 添加副标题
    subtitle_box = slide.shapes.add_textbox(
        Inches(1), Inches(4), Inches(8), Inches(1)
    )
    tf = subtitle_box.text_frame
    p = tf.paragraphs[0]
    p.text = "Daily Digest"
    p.alignment = PP_ALIGN.CENTER
    set_text_style(tf, 'Microsoft YaHei', 28, color=(44, 82, 130))
    
    return slide

def create_content_slide(prs, number, en_title, cn_title, abstract, journal, date):
    """创建内容页"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # 英文标题
    title_box = slide.shapes.add_textbox(
        Inches(0.8), Inches(0.8), Inches(8.4), Inches(0.8)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = f"{number}. {en_title}"
    set_text_style(tf, 'Microsoft YaHei', 20, bold=True, color=(26, 54, 93))
    
    # 中文标题
    cn_box = slide.shapes.add_textbox(
        Inches(0.8), Inches(1.6), Inches(8.4), Inches(0.5)
    )
    tf = cn_box.text_frame
    p = tf.paragraphs[0]
    p.text = cn_title
    set_text_style(tf, 'Microsoft YaHei', 16, color=(74, 85, 104))
    
    # 摘要
    abs_box = slide.shapes.add_textbox(
        Inches(0.8), Inches(2.3), Inches(8.4), Inches(3.5)
    )
    tf = abs_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = abstract
    set_text_style(tf, 'Microsoft YaHei', 14, color=(45, 55, 72))
    
    return slide
```

## ✅ 质量检查清单

- [ ] 标题字号大于正文
- [ ] 颜色搭配协调
- [ ] 每页内容不溢出
- [ ] 中英文标题对应
- [ ] 摘要精炼但完整
- [ ] 页码正确
- [ ] 动画简洁（如有）
- [ ] 整体风格统一
