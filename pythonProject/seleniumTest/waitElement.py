#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : waitElement.py
@Time    : 2019/1/3 16:37
@desc   : 显示等待
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

option=webdriver.ChromeOptions()
option.add_argument('headless')
browser=webdriver.Chrome(options=option)

browser.get('http://www.taobao.com')
wait=WebDriverWait(browser,10)
input=wait.until(EC.presence_of_element_located((By.ID, 'q' )))

button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))

print(input,button)