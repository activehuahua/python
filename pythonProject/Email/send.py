from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.mime.application import MIMEApplication
#msg=MIMEText('hello,send by Python...','plain','utf-8')
#msg = MIMEText('<html><body><h1>Hello</h1>' +
#    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#    '</body></html>', 'html', 'utf-8')

msg = MIMEMultipart()

# 输入Email地址和口令:
# from_addr = input('From: ')
# password = input('Password: ')
# 输入收件人地址:

from_addr ='jianghua_zhao@163.com'
password = 'Cdzjh730815'
to_addr = '164033495@qq.com'
# 输入SMTP服务器地址:
#smtp_server = input('SMTP server: ')
smtp_server = 'smtp.163.com'

import smtplib
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
# 邮件正文是MIMEText:
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
      '<p><img src="cid:0"></p>'+
     '</body></html>', 'html', 'utf-8'))


# 邮件正文嵌入图片
with open('me.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='me.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='me.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

#发送附件
part = MIMEApplication(open('me.jpg', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='me.jpg')
msg.attach(part)


# part = MIMEApplication(open('显示器.txt', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename='显示器.txt')
# msg.attach(part)

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()