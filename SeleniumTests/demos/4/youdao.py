# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 18:46
# @Author  : zhaojianghua
# @File    : youdao.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.youdao.com")

driver.find_element_by_id('translateContent').send_keys('hello')
driver.find_element_by_id('translateContent').submit()

driver.quit()