#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : amstl-num.py
@Time    : 2018/12/6 16:38
'''

lower_num = 1
upper_num = 10000

for i in range(lower_num, upper_num + 1):
    n = len(str(i))
    temp = i
    sum = 0
    while temp > 0:
        digit_num = temp % 10
        sum += digit_num ** n
        temp //= 10
    if (i == sum):
        print(i)
