# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 17:08
# @Author  : zhaojianghua
# @File    : execise.py
# @Software: PyCharm
# @Desc    :

import numpy as np
import pandas as pd
from pandas import DataFrame

data={
    'Chinese':[66,95,95,90,80,80],
    'English':[65,85,92,88,90,90],
    'Math':[None,98,96,77,90,90]
}

df=DataFrame(data,index=[u'张飞',u'关于',u'赵云',u'黄忠',u'典韦',u'典韦'],columns=['Chinese','English','Math'])

df=df.drop_duplicates()

#if df.isnull().any()==True:

#有空值None的地方默认替换成0
df=df.fillna(0)

df['Total']=df.sum(axis=1)
df.rename(columns={'Chinese':u'语文','English':u'英语','Math':u'数学','Total':u'总分'},inplace=True)

print(df)