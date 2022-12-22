
# -*- coding: utf-8 -*-#

'''
# Name:         linePredict
# Description:  
# Author:       alex
# Date:         2022/7/7
'''

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y = [74.9,74.5,74.95,75.2,75.2,74.4,74.8,74.85,74.35,74.25,74.25,74.3,74,74.25,74.35]
print(np.ones(2))

# 增加维度
A = np.vstack([x, np.ones(len(x))]).T
# 调用最小二乘法函数
a, b = np.linalg.lstsq(A, y)[0]
# 转换成numpy array
x = np.array(x)
y = np.array(y)
# 画图
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, a * x + b, 'r', label='fitted line')
print(a,b)
for i in range(16,23):
    result=a*i+b
    print (i,result)
plt.show()



