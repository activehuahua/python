# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 11:17
# @Author  : zhaojianghua
# @File    : 6.py
# @Software: PyCharm
# @Desc    : 中位数，平均数 ,median,mean,average

import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# 求中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
# 求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

# 求平均数
print(np.average(a))
print(np.average(a, axis=0))
print(np.average(a, axis=1))
