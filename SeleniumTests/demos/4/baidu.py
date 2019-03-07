# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 18:49
# @Author  : zhaojianghua
# @File    : baidu.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

size=driver.find_element_by_id('kw').size
print(size)

text=driver.find_element_by_id('cp').text
print(text)

attribute=driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

result=driver.find_element_by_id('kw').is_displayed()
print(result)

driver.quit()