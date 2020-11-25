# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 10:53
# @Author  : zhaojianghua
# @File    : sendReport.py
# @Software: PyCharm
# @Desc    :

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def SENDMAIL(to,cc, filename):
    print("开始发送邮件.....")
    # 邮件用户
    _user = 'alexander.zhao@silksoftware.com'
    _pwd = "Alexander_2019"

    # 如名字所示Multipart就是分多个部分
    msg = MIMEMultipart()
    msg["Subject"] = '主题：H&M Bug统计'
    msg["From"] = _user
    msg["To"] = ",".join(to)
    msg["cc"] = ",".join(cc)
    #抄送
    #msg["Cc"] = ",".join(to)

    # ---这是文字部分---
    part = MIMEText('\n'
                    '你好， \n'
                    '    H&M Bug统计详情请见附件\n'
                    '    ',_charset='utf-8')
    msg.attach(part)

    # ---这是附件部分---
    # xlsx类型附件
    part = MIMEApplication(open(filename, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(part)

    s = smtplib.SMTP("mbox.silksoftware.com", 587)  # 连接smtp邮件服务器,端口默认是25
    s.starttls()
    #s.set_debuglevel(1)
    s.login(_user, _pwd)  # 登陆服务器

    receive=to
    receive.extend(cc)
    s.sendmail(_user, to, msg.as_string())  # 发送邮件
    s.close()
    print("邮件发送完毕！")

if __name__ == '__main__':
    to=['164033495@qq.com']
    cc=['alexander.zhao@silksoftware.com']
    filename="config.py"
    SENDMAIL(to,to,filename)