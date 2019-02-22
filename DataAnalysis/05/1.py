# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 15:35
# @Author  : zhaojianghua
# @File    : 1.py
# @Software: PyCharm
# @Desc    :

import pandas as pd
from pandas import Series, DataFrame
x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)
