#!/usr/bin/python3
# -*-coding:utf-8 -*-
##**********************************************
# @Time     : 2019/8/19 10:02
# @Author   : alex.zhao
# @File     : sendEmail.py
# @User     : silk
# @Software: PyCharm
##**********************************************

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From']= '15002803902@163.com'
    msg['To']= '1181077095@qq.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("", "")
    smtp.sendmail("15002803902@163.com","1181077095@qq.com",msg.as_string())
    smtp.quit()
    print('email has send out!')

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new
