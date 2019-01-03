#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : exceptions.py
@Time    : 2019/1/3 18:23
@desc   : 异常处理
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

browser=webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time out')

try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No element!')
finally:
    browser.close()
