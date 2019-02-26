# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 15:47
# @Author  : zhaojianghua
# @File    : food.py
# @Software: PyCharm
# @Desc    :

import pandas as pd
from pandas import DataFrame

df=pd.read_excel('food.xlsx')
print(df)

#小写food名称
df['food']=df['food'].str.lower()
print(df)

#取绝对值，去掉负数
df['ounces']=df['ounces'].apply(lambda  x : abs(x))
print(df)

#取food名称一致的行
d_rows=df[df['food'].duplicated(keep=False)]
#按food名称，取平均值
g_items=d_rows.groupby('food').mean()
print(g_items)

#遍历分组值，对food名的值进行改写
for i,row in g_items.iterrows():
    #此处row只能用name取出food值
    df.loc[df['food'] ==row.name ,'ounces']=row.ounces
    print(row.name,row.ounces  )

#去掉food列的重复值
df.drop_duplicates('food',inplace=True)

#重新进行行的index排序
df.index=range(len(df))
print(df)