# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 9:11
# @Author  : zhaojianghua
# @File    : 2.py
# @Software: PyCharm
# @Desc    :结构数组，计算平均分
#
#
import numpy as np
persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)

#统计某一维数据
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']

#求平均数
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))

#求和
print(np.sum(ages))
print(np.sum(chineses))
print(np.sum(maths))
print(np.sum(englishs))
