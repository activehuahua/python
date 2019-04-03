# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 11:39
# @Author  : zhaojianghua
# @File    : cookie.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.youdao.com")

cookie=driver.get_cookies()

driver.add_cookie({'name':'key-aaaaaa','value':'value-bbbbbb'})

for cook in driver.get_cookies():
    print("%s -> %s"%(cook['name'],cook['value']))
print(cookie)

driver.quit()