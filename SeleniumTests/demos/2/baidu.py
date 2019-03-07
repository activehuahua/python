# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 14:38
# @Author  : zhaojianghua
# @File    : baidu.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium3")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()