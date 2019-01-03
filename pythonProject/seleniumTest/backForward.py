#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : backForward.py
@Time    : 2019/1/3 17:14
@desc   :
'''

from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get('http://www.baidu.com')
time.sleep(1)
browser.get('http://www.taobao.com')
time.sleep(1)
browser.get('http://www.sohu.com')
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
browser.close()