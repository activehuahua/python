#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : smtp-ep1.py
@Time    : 2018/12/13 15:55
@desc   :
'''
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

sender = 'ops@pretang.com'
receivers = ['zhaojianghua@pretang.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEMultipart()
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
message['To'] = Header("测试", 'utf-8')  # 接收者
content = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
content=MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><br>good!','html','utf-8')
message.attach(content)
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

filename = 'smtp-ep1.py'
att = MIMEApplication(open(filename, 'rb').read())
att.add_header('Content-Disposition', 'attachment', filename=filename)

# att = MIMEText(open('smtp-ep1.py', 'rb').read(), 'base64', 'utf-8')
# att["Content-Type"] = 'application/octet-stream'
# att["Content-Disposition"] = 'attachment; filename="smtp-ep1.py"'

message.attach(att)
try:
    smtpObj = smtplib.SMTP('smtp.exmail.qq.com')
    smtpObj.login('ops@pretang.com', 'Chutang123')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
