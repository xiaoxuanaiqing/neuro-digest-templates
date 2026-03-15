# 🧠 Neuroscience Daily Digest 模板系统

> 自动化神经科学文献每日摘要生成系统

## 📋 项目概述

本项目用于从 [Planet Neuroscience](https://neuroblog.fedoraproject.org/planet-neuroscience) 爬取最新神经科学文献，自动生成格式化的：
- 📄 **Word 文档**（简约高级风格）
- 🎨 **PowerPoint 演示文稿**
- 📧 **邮件发送**

## 📁 文件结构

```
neuro-digest-templates/
├── README.md                      # 本文件
├── templates/                     # 模板文件
│   ├── markdown_template.md      # Markdown 内容模板
│   ├── word_style_guide.md       # Word 排版规范
│   └── ppt_style_guide.md        # PPT 排版规范
├── scripts/                       # 自动化脚本
│   ├── generate_word.py          # 生成 Word 文档
│   ├── generate_ppt.py           # 生成 PPT 文档
│   ├── send_email.py             # 发送邮件
│   └── fetch_papers.py           # 爬取文献
├── examples/                      # 示例文件
│   └── sample_digest.md          # 示例摘要
├── assets/                        # 资源文件
│   └── logo.png                  # 可选：Logo图片
└── .gitignore                     # Git 忽略规则
```

## 🎨 排版规范

### Word 文档
- **字体标题**: 思源黑体/微软雅黑 Bold, 18pt, 深蓝 (#1a365d)
- **字体正文**: 思源黑体/微软雅黑 Regular, 11pt, 深灰 (#2d3748)
- **行距**: 1.5 倍行距
- **边距**: 上下 2.5cm, 左右 3cm
- **每篇文章格式**:
  - 序号 + 英文标题 (Bold, 14pt)
  - 中文翻译 (Italic, 12pt, 灰色)
  - 摘要正文 (11pt)
  - 来源信息 (10pt, 灰色, 斜体)

### PPT 演示文稿
- **主题**: 简约学术风格，白底深蓝字
- **标题页**: 日期 + 总文章数
- **内容页**: 每页 1-2 篇文章
- **字体**: 标题 24pt, 正文 18pt
- **配色**: 主色 #1a365d, 辅色 #718096

### 邮件格式
- **主题**: `Neuroscience Daily Digest | YYYY-MM-DD`
- **正文**: 简要统计信息
- **附件**: Word + PPT 双版本
- **MIME类型**:
  - Word: `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
  - PPT: `application/vnd.openxmlformats-officedocument.presentationml.presentation`

## 🚀 使用方法

### 1. 安装依赖
```bash
pip install python-docx python-pptx beautifulsoup4 requests
```

### 2. 爬取文献
```bash
python scripts/fetch_papers.py --output today.md
```

### 3. 生成文档
```bash
# 生成 Word
python scripts/generate_word.py --input today.md --output digest.docx

# 生成 PPT
python scripts/generate_ppt.py --input today.md --output digest.pptx

# 生成全部
python scripts/generate_all.py --input today.md
```

### 4. 发送邮件
```bash
python scripts/send_email.py --docx digest.docx --pptx digest.pptx
```

## ⚙️ 配置文件

创建 `config.json`:
```json
{
  "email": {
    "smtp_server": "smtp.qq.com",
    "smtp_port": 587,
    "sender": "your_email@qq.com",
    "receiver": "receiver@example.com"
  },
  "style": {
    "primary_color": "#1a365d",
    "secondary_color": "#718096",
    "font_title": "Microsoft YaHei",
    "font_body": "Microsoft YaHei"
  }
}
```

## 📝 内容要求

- ✅ 每篇文章必须包含完整标题（英文+中文）
- ✅ 摘要内容完整，不得删减
- ✅ 标注来源期刊和日期
- ✅ 简约高级风格排版

## 📊 统计信息

每日摘要包含：
- 总文章数
- 来源期刊分布
- 研究主题分类（可选）

## 🔒 隐私说明

- 邮件凭证存储在环境变量或 `.env` 文件中
- 不提交敏感信息到 GitHub

## 📅 更新日志

- **2026-03-15**: 初始模板系统创建

---

**维护者**: xiaoxuanaiqing  
**用途**: 每日神经科学文献跟踪与分享
