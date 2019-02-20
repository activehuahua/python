# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 8:58
# @Author  : zhaojianghua
# @File    : 1.py
# @Software: PyCharm
# @Desc    : 数组声明、赋值及打印

import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1,1]=10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)
