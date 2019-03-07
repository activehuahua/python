# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 18:18
# @Author  : zhaojianghua
# @File    : initBase.py
# @Software: PyCharm
# @Desc    :
from selenium import  webdriver

class baseClass():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://partner.fc.igemi.cn")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)