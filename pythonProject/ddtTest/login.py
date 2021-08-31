#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : login.py
@Time    : 2019/8/13 10:05
@desc   :
'''

import ddt
from selenium import webdriver


browser = webdriver.Chrome()
browser.maximize_window()
username = "hmuat"  # stands for !@user
password = "go4uat"  # stands for ^&pass
url='ec.qingmutec.com'
webUrl = 'https://{}:{}@{}'.format(username, password, url)
browser.get(webUrl)


login_url='https://{}:{}@{}'.format(username, password, "ec.qingmutec.com/en_cn/customer/account/login/")

browser.get(login_url)

closeButton = browser.find_element_by_class_name('action-close')
closeButton.click()

email=browser.find_element_by_id('email')
password=browser.find_element_by_id('pass')
login=browser.find_element_by_id('send2')


#print(loginResult)

# /email.send_keys('18086846185')
# password.send_keys('1245555')
# login.click()
#print(loginResult)


email.send_keys('164033495@qq.com')
password.send_keys('Mi123456')
login.click()
loginResult=browser.find_element_by_xpath('//div[@class="session-menu"]/ul/a/li[@class="user-regs  login_act "]/span')

print(loginResult)
print(loginResult.text)


