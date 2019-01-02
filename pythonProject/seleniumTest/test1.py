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
# print(browser.current_url)
# print(browser.page_source)
#browser.close()

#browser.find_element_by_id('kw').send_keys('python')
#browser.find_element_by_class_name('s_ipt').send_keys('python')
#browser.find_element_by_css_selector('#kw').send_keys('python')
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
browser.find_element_by_id('su').click()