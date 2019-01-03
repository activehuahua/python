#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : browserTabs.py
@Time    : 2019/1/3 18:13
@desc   : 操作浏览器tab，新开窗口，切换窗口
'''

from selenium import webdriver

browser = webdriver.Chrome( )
browser.maximize_window( )
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)

browser.switch_to.window(browser.window_handles[ 1 ])
browser.get('http://www.taobao.com')

browser.switch_to.window(browser.window_handles[ 0 ])
browser.get('http://www.sohu.com')
