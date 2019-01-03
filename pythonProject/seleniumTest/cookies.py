#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : cookies.py
@Time    : 2019/1/3 17:27
@desc   :
'''
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())

browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germy'})
print(browser.get_cookies())

browser.delete_all_cookies()
print(browser.get_cookies())