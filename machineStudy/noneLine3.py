
# -*- coding: utf-8 -*-#

'''
# Name:         noneLine2
# Description:  
# Author:       alex
# Date:         2022/7/7
'''
from pandas import read_csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

plt.rcParams['font.family']='SimHei'#解决中文字体
data=read_csv('testValue.csv',encoding='UTF-8')
plt.scatter(data.day, data.number)

data.corr()
lrModel=LinearRegression()
x=data[['day']]
y=data[['number']]
plt.scatter(x,y)
plt.xlabel('日期')
plt.ylabel('数量')
plt.show()

from sklearn.preprocessing import PolynomialFeatures as pf
pd=pf(degree=5)
x1=pd.fit_transform(x)
irmodle=LinearRegression()
irmodle.fit(x1,y)
a=irmodle.score(x1,y)
b=pd.fit_transform([[18]])
c=irmodle.predict(b)
print(a)
# print("预计16日的感染人数为",irmodle.predict(pd.fit_transform([[17]])))
# print("预计17日的感染人数为",c)
# print("预计3/31日的感染人数为",irmodle.predict(pd.fit_transform([[19]])))
# print("预计4/1日的感染人数为",irmodle.predict(pd.fit_transform([[20]])))

for i in range(16,23):
    print(i,irmodle.predict(pd.fit_transform([[i]])))