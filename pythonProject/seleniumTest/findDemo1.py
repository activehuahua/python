#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : findDemo1.py
@Time    : 2019/5/8 10:21
@desc   :
'''

from selenium import  webdriver
from selenium.webdriver.common.by import By

html='''
<h4 class="cart-item-name"><a href="https://rays-store8.mybigcommerce.com/modern-hardware-bundle-for-double-walk-through-gates/">Modern Hardware Bundle for Double Walk Through Gates</a></h4>
'''

driver=webdriver.Chrome()

driver.find_element_by_xpath()
