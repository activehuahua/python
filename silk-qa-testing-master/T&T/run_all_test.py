import unittest, time
from HTMLTestRunner import HTMLTestRunner
import os, io
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from model.sendEmail import new_report, send_mail

curPath = os.path.abspath(os.path.dirname(__file__))
test_dir = curPath + '\\TestCase\\'
test_report = curPath + '\\report\\'

print(test_dir,',',test_report)
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_case.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description="运行环境：windows 7, chrome")
    runner.run(discover)
    fp.close()

    # new_report = new_report(test_report)
    # send_mail(new_report)
