#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : quote-配.py
@Time    : 2018/12/12 13:59
@desc   : 转变URL格式编码
'''

from urllib.parse import quote,unquote

keyword='壁纸'
url='https://www.baidu.com/s?wd='+quote(keyword)
print(url)

#url='https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))