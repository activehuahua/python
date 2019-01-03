#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : scriptAction.py
@Time    : 2019/1/3 15:54
@desc   :
'''

from selenium import webdriver

#静默模式，不打开浏览器
option=webdriver.ChromeOptions()
option.add_argument('headless')
browser=webdriver.Chrome(options=option)

browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 滑动滚动条到底部
#browser.execute_script('alert("To Bottom")')
#隐式等待
browser.implicitly_wait(10)
#找 提问 按钮
input=browser.find_element_by_id('zu-top-add-question')
print(input)
#获取元素class属性
print(input.get_attribute('class'))
#元素内部文字
print(input.text)
#元素的坐标位置
print(input.location)
# 标签类型
print(input.tag_name)
# 元素的尺寸
print(input.size)