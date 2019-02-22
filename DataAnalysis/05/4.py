# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 16:38
# @Author  : zhaojianghua
# @File    : 4.py
# @Software: PyCharm
# @Desc    :清除前后空格

import numpy as np
import pandas as pd
from pandas import DataFrame

data = {'Chinese': ['66', ' 95 ', '93 ','  90','80'],'English': [65, 85, 92, 88, 90],'Math': ['$30', '$98', '$96', '$77', '$90']}
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])


df2=df2.drop_duplicates() #去掉重复的行

#清除前后空格
df2['Chinese']=df2['Chinese'].map(str.strip)

#清除具体字符
df2['Math']=df2['Math'].str.strip('$')

def double_df(x):
    return x*2

df2['English']=df2['English'].apply(double_df)
print(df2)