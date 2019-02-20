# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 9:38
# @Author  : zhaojianghua
# @File    : 3.py
# @Software: PyCharm
# @Desc    :arange() 初始值、终值、步长#  等差数列
#           linspace 初始值、终值、元素个数，等差数列
# remainder  求余函数，同 mod


import numpy as np
a=np.arange(1,11,2)
b=np.linspace(1,8,5)
print(a)
print(b)

x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))
