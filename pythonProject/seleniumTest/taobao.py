#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : taobao.py
@Time    : 2019/1/2 17:58
@desc   :
'''

from selenium import webdriver
import  time

browser= webdriver.Chrome()
browser.get("https://www.taobao.com")
lis=browser.find_elements_by_css_selector('.service-bd li')

print(lis)

input=browser.find_element_by_id('q')
input.send_keys('ipad')

browser.find_element_by_class_name('btn-search').click()