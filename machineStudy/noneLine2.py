
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
data=read_csv('2.csv',encoding='GBK')
plt.scatter(data.day,data.number)


# data= pd.read_csv('2.csv')
# X_test = data.loc[:,'日期']
# y_test = data.loc[:,'感染人数']

data.corr()
lrModel=LinearRegression()
x=data[['day']]
y=data[['number']]
plt.scatter(x,y)
plt.xlabel('日期序数')
plt.ylabel('感染人数')
plt.show()

from sklearn.preprocessing import PolynomialFeatures as pf
pd=pf(degree=3)
x1=pd.fit_transform(x)
irmodle=LinearRegression()
irmodle.fit(x1,y)
a=irmodle.score(x1,y)
b=pd.fit_transform([[18]])
c=irmodle.predict(b)
print(a)
print("预计3/29日的感染人数为",irmodle.predict(pd.fit_transform([[17]])))
print("预计3/30日的感染人数为",c)
print("预计3/31日的感染人数为",irmodle.predict(pd.fit_transform([[19]])))
print("预计4/1日的感染人数为",irmodle.predict(pd.fit_transform([[20]])))