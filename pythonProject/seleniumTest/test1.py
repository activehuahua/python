#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : test1.py
@Time    : 2018/12/7 11:57
@desc   :
'''

from selenium import webdriver

browser=webdriver.Chrome()
# browse=webdriver.Firefox()

browser.get('https://www.baidu.com')
print(browser.current_url)
