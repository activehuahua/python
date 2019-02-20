# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 11:20
# @Author  : zhaojianghua
# @File    : 7.py
# @Software: PyCharm
# @Desc    : 加权平均 (1*1+2*2+3*3+4*4)/(1+2+3+4)=3
#

import numpy as np

a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print(np.average(a))
print(np.average(a,weights=wts))
