# 🧠 Neuroscience Daily Digest 模板系统

> 自动化神经科学文献每日摘要生成系统 - 标准版

## 📋 项目概述

本项目用于从 [Planet Neuroscience](https://neuroblog.fedoraproject.org/planet-neuroscience) 爬取最新神经科学文献，自动生成格式化的：
- 📄 **Word 文档**（简约学术风格）
- 📧 **邮件发送**（HTML正文 + Word附件）

## 📁 文件结构

```
neuro-digest-templates/
├── README.md                      # 本文件
├── scripts/                       # 自动化脚本
│   ├── generate_word.py          # 生成 Word 文档（标准格式）
│   ├── send_email.py             # 发送邮件（HTML+附件）
│   └── fetch_papers.py           # 爬取文献（待实现）
├── templates/                     # 模板规范
│   └── format_spec.md            # 格式规范文档
├── examples/                      # 示例文件
│   └── sample_articles.json      # 示例文章数据
└── .gitignore                     # Git 忽略规则
```

## 🎨 Word 文档格式规范（标准版）

| 元素 | 格式 |
|------|------|
| **主标题** | Times New Roman + 微软雅黑, 18pt, 蓝色(#000080), 居中 |
| **副标题** | Times New Roman + 微软雅黑, 12pt, 灰色, 斜体, 居中 |
| **文章标题** | Times New Roman, 14pt, 斜体, 黑色 |
| **来源** | Times New Roman, 10pt, 灰色(#505050) |
| **英文摘要标题** | "Abstract (English)", 11pt, 粗体, 深蓝(#003366) |
| **英文摘要内容** | Times New Roman, 10.5pt, 1.15倍行距 |
| **中文摘要标题** | "中文摘要", 11pt, 粗体, 深红(#8B0000) |
| **中文摘要内容** | Times New Roman + 宋体, 10.5pt, 1.15倍行距 |
| **分隔线** | 灰色虚线 "─" × 60 |
| **页脚** | 9pt, 灰色, 斜体, 居中 |

### 邮件格式规范

| 元素 | 格式 |
|------|------|
| **主题** | `📰 Neuroscience Daily Digest | YYYY-MM-DD` |
| **正文** | HTML 格式，简约卡片风格 |
| **附件** | Word 文档 (.docx) |
| **附件MIME类型** | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |

## 🚀 使用方法

### 1. 安装依赖

```bash
pip install python-docx
```

### 2. 准备文章数据

创建 `articles.json`:
```json
[
  {
    "title": "Article Title in English",
    "source": "arXiv: q-bio.NC",
    "date": "2026-03-15",
    "abstract": "English abstract...",
    "translated": "中文摘要..."
  }
]
```

### 3. 生成 Word 文档

```bash
cd neuro-digest-templates/scripts

# 从Markdown生成
python generate_word.py --input articles.md --output digest.docx
```

### 4. 发送邮件

```bash
# 设置环境变量
export EMAIL_SENDER='your_email@qq.com'
export EMAIL_PASSWORD='your_auth_code'
export EMAIL_RECEIVER='receiver@qq.com'

# 发送邮件
python send_email.py --docx digest.docx --articles articles.json
```

## 📝 文章数据格式

### Markdown 格式
```markdown
### 1. Article Title
*中文标题*

**摘要**：英文摘要内容...

📄 *Source* | 2026-03-15
```

### JSON 格式
```json
{
  "title": "English Title",
  "source": "Journal Name",
  "date": "2026-03-15",
  "abstract": "English abstract...",
  "translated": "中文摘要..."
}
```

## 🔒 隐私说明

- 邮件凭证存储在环境变量中
- 不提交敏感信息到 GitHub
- 建议使用 QQ 邮箱授权码而非密码

## 📅 更新日志

- **2026-03-15**: 标准版模板系统创建
  - 基于 2026-03-13 版本优化
  - 统一字体和配色规范
  - 简化使用流程

---

**维护者**: xiaoxuanaiqing  
**用途**: 每日神经科学文献跟踪与分享
