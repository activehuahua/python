# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 11:41
# @Author  : zhaojianghua
# @File    : sorting.py
# @Software: PyCharm
# @Desc    :sort(a, axis=-1, kind=‘quicksort’, order=None) 默认最后一个轴排序，默认快速排序
#                                  quicksort、mergesort、heapsort

import numpy as np
a = np.array([[4,3,2],[2,4,1]])
print(np.sort(a))
print(np.sort(a, axis=None))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))
