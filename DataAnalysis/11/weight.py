# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 14:24
# @Author  : zhaojianghua
# @File    : weight.py
# @Software: PyCharm
# @Desc    :
import pandas as pd
from pandas import DataFrame
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
#pd.set_option('max_colwidth',200)
#DataFrame 打印结果不换行方法
pd.set_option('display.width', 5000)

df=pd.read_csv('weight1.csv',header=None)
#print(type(df))
#df.round(2)
print(df)
df.columns=['id','fullname','age','weight','data1','data2','data3','data4','data5','data6']

# 删除全空的行
df.dropna(how='all',inplace=True)
#print(df)

df['age'].fillna(df['age'].mean(),inplace=True)

#df.round({'age':2})


# 获取 weight 数据列中单位为 lbs 的数据
rows_with_lbs = df['weight'].str.contains('lbs').fillna(False)
#print(df[rows_with_lbs])
# 将 lbs 转换为 kgs, 2.2lbs=1kgs
for i,lbs_row in df[rows_with_lbs].iterrows():
	# 截取从头开始到倒数第三个字符之前，即去掉 lbs。
	weight = int(float(lbs_row['weight'][:-3])/2.2)

# 重新赋值
	df.at[i,'weight'] = '{}kgs'.format(weight)

print(df)
#出现频次最多的数值
weight_maxf=df['weight'].value_counts().index[0]
df['weight'].fillna(weight_maxf,inplace=True)



#print(df)
#df['new1']=df['fullname'].str.split()
df[['first_name','last_name']]=df['fullname'].str.split(expand=True)
df.drop('fullname',axis=1, inplace=True)

new_columns=['id','first_name','last_name','age','weight','data1','data2','data3','data4','data5','data6']
df=df.reindex(columns=new_columns)
print(df)
# 删除重复数据行
df.drop_duplicates(['first_name','last_name'],inplace=True)
df.to_excel('RESULT.xlsx')
print(df)