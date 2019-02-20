# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 10:49
# @Author  : zhaojianghua
# @File    : 5.py
# @Software: PyCharm
# @Desc    :ptp 求最大值与最小值的差值
#           percentile 求百分位数，0-100,0取最小值，100取最大值，50取中间数
#将数组array从小到大排序，计算(n-1)*p的整数部分为i，小数部分为j，其中n为数组大小，
# 则percentile的值是：(1-j)*array（第i+1个数） + j*array（第i+2个数）。
# 如1,4,7 求30的百分位数   (3-1)*0.3=0.6， i=0,j=0.6   (1-0.6)*A(1)+0.6*A(2)=0.4*1+0.6*4=2.8

import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))


a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.percentile(a, 30))
print(np.percentile(a, 50))
print(np.percentile(a, 30, axis=0))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))
