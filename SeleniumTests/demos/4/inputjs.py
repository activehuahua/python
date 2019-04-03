# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 15:21
# @Author  : zhaojianghua
# @File    : inputjs.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

text="input text"
js= "var sum=document.getElementById('kw'); sum.value='"+text+"';"
driver.execute_script(js)