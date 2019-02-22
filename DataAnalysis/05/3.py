# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 16:08
# @Author  : zhaojianghua
# @File    : 3.py
# @Software: PyCharm
# @Desc    : 数据清洗 drop去掉列columns，去掉索引 index
#            rename 改显示名称

import numpy as np
import pandas as pd
from pandas import DataFrame

data = {'Chinese': [66,  95 , 93 ,  90,80],'English': [65, 85, 92, 88, 90],'Math': [30, 98, 96, 77, 90]}
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])

df2=df2.drop(columns=['Math'])
df2=df2.drop(index=['HuangZhong'])
#df2.rename(columns={'Chinese':'yuwen','English':'yingyu'},inplace=True)

df2=df2.drop_duplicates() #去掉重复的行
print(df2.dtypes)

def plus(df,n,m):
    df['new1'] = (df['Chinese']+df['English']) * m
    df['new2'] = (df['Chinese']+df['English']) * n
    return df
df1 = df2.apply(plus,axis=1,args=(2,3,))
print(df1)
