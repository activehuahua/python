#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : re-ep5.py
@Time    : 2018/12/14 15:42
@desc   :
'''

import  re

str='Hello 124343 fdsfjdDemo'

result=re.match('^He.*?(\d+).*Demo$',str)
print(result.group())
print(result.group(1))