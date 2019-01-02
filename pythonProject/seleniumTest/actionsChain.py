#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : actionsChain.py
@Time    : 2019/1/2 18:07
@desc   : 用selenium 完成模拟人工操作
'''

from selenium import webdriver
from selenium.webdriver import  ActionChains

browser=webdriver.Chrome()
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

browser.get(url)
browser.switch_to.frame('iframeResult')
source=browser.find_element_by_id('draggable')
target=browser.find_element_by_id('droppable')

actions=ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()