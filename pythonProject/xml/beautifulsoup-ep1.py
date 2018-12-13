#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : beautifulsoup-ep1.py
@Time    : 2018/12/7 13:57
@desc   :
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup('<a>Hello</a>', 'lxml')

print(soup.a.string)
