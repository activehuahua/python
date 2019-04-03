# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 11:47
# @Author  : zhaojianghua
# @File    : baiduScroll.py
# @Software: PyCharm
# @Desc    :
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.set_window_size(800,600)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

time.sleep(2)

js='window.scrollTo(100,450);'

driver.execute_script(js)

time.sleep(3)

