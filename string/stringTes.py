
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : stringTes.py
@Time    : 2018/11/15 15:41
'''

import  string

str1='fff2222'

print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())

#for x  in [1, 2, 3]: print(x**2, end=" ")

l1={x**2 for x in (2, 4, 6,8)}
print(l1)
l2=list(l1)
l2.sort()
print(l2)