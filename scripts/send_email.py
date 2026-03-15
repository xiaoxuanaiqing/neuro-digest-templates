#!/usr/bin/env python3
"""
发送 Neuroscience Daily Digest 邮件
支持 Word 和 PPT 双附件
"""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

class EmailSender:
    """邮件发送器"""
    
    def __init__(self, smtp_server='smtp.qq.com', smtp_port=587):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender = os.environ.get('EMAIL_SENDER', 'your_email@qq.com')
        self.password = os.environ.get('EMAIL_PASSWORD', 'your_auth_code')
        self.receiver = os.environ.get('EMAIL_RECEIVER', self.sender)
    
    def send_digest(self, docx_path, pptx_path, date_str=None):
        """发送每日摘要邮件"""
        if date_str is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
        
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Subject'] = f'Neuroscience Daily Digest | {date_str}'
        
        # 邮件正文
        body = f"""您好！

今日神经科学文献精选已为您整理好。

📄 附件包含：
   • Word 完整版（适合阅读、批注）
   • PowerPoint 演示版（适合汇报、分享）

内容来源于 Planet Neuroscience，
精选最新神经科学研究进展。

祝您阅读愉快！

---
Neuroscience Daily Digest System
{date_str}
"""
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 添加 Word 附件
        if docx_path and os.path.exists(docx_path):
            with open(docx_path, 'rb') as f:
                docx_attachment = MIMEApplication(f.read())
                docx_attachment.add_header(
                    'Content-Disposition', 
                    'attachment', 
                    filename=os.path.basename(docx_path)
                )
                msg.attach(docx_attachment)
        
        # 添加 PPT 附件
        if pptx_path and os.path.exists(pptx_path):
            with open(pptx_path, 'rb') as f:
                pptx_attachment = MIMEApplication(f.read())
                pptx_attachment.add_header(
                    'Content-Disposition', 
                    'attachment', 
                    filename=os.path.basename(pptx_path)
                )
                msg.attach(pptx_attachment)
        
        # 发送邮件
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receiver, msg.as_string())
            server.quit()
            print(f"✅ 邮件发送成功！收件人: {self.receiver}")
            return True
        except Exception as e:
            print(f"❌ 邮件发送失败: {e}")
            return False


def main():
    """主函数"""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='发送 Neuroscience Daily Digest 邮件')
    parser.add_argument('--docx', help='Word文档路径')
    parser.add_argument('--pptx', help='PPT文档路径')
    parser.add_argument('--date', help='日期 (YYYY-MM-DD)', default=None)
    
    args = parser.parse_args()
    
    # 检查环境变量
    if not os.environ.get('EMAIL_PASSWORD'):
        print("⚠️ 请设置环境变量 EMAIL_PASSWORD")
        print("示例: export EMAIL_PASSWORD='your_auth_code'")
        return
    
    sender = EmailSender()
    sender.send_digest(args.docx, args.pptx, args.date)


if __name__ == '__main__':
    main()
