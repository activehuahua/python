# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 10:40
# @Author  : zhaojianghua
# @File    : 4.py
# @Software: PyCharm
# @Desc    :  0 代表y轴，1代表x轴  amin 取最小值，amax 取最大值

import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.amin(a))
print(np.amin(a,0))  # 1,4,7  2,5,8  3,6,9
print(np.amin(a,1))  # 1,2,3  4,5,6  7,8,9
print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))
