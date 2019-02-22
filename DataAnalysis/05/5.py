# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 16:53
# @Author  : zhaojianghua
# @File    : 5.py
# @Software: PyCharm
# @Desc    :  数据合并
import pandas as pd
from pandas import DataFrame

df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data1':range(5)})

print(df1.describe())

df3=pd.merge(df1,df2,on='name')
print(df3)

df3=pd.merge(df1,df2,how='inner')
print(df3)

df3=pd.merge(df1,df2,how='left')
print(df3)

df3=pd.merge(df1,df2,how='right')
print(df3)

df3=pd.merge(df1,df2,how='outer')
print(df3)