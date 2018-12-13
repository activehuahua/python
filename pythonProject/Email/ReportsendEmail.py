#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"
import smtplib
import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def SENDMAIL(to, filename):
    print("开始发送邮件.....")
    # 邮件用户
    _user = 'hengxiang@pretang.com'
    _pwd = "Chutang123"

    # 如名字所示Multipart就是分多个部分
    msg = MIMEMultipart()
    msg["Subject"] = filename
    msg["From"] = _user
    msg["To"] = ",".join(to)

    # ---这是文字部分---
    part = MIMEText('\n'
                    '你好， \n'
                    '    详情请见附件\n'
                    '    这是一封自动发送的邮件,勿回复。 \n')
    msg.attach(part)

    # ---这是附件部分---
    # xlsx类型附件
    part = MIMEApplication(open(filename, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(part)

    s = smtplib.SMTP("smtp.exmail.qq.com", timeout=60)  # 连接smtp邮件服务器,端口默认是25
    s.login(_user, _pwd)  # 登陆服务器
    s.sendmail(_user, to, msg.as_string())  # 发送邮件
    s.close()
    print("邮件发送完毕！")
