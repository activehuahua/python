
# -*- coding: utf-8 -*-#

'''
# Name:         linePredict2
# Description:  
# Author:       alex
# Date:         2022/7/7
'''
### 例子2：线性回归2
import pandas as pd
import numpy as np
data_train = pd.read_csv('testValue.csv')
data_train.head()#展示头部数据

#定义训练数据
X_train = data_train.loc[:, "T"]
y_train = data_train.loc[:, 'R']

#训练数据可视化
#%matplotlib inline
from matplotlib import pyplot as plt
fig1 = plt.figure(figsize=(5,5))
plt.scatter(X_train,y_train)
plt.title('raw data')
plt.xlabel('temperature')
plt.ylabel('rate')
#plt.show()

X_train = np.array(X_train).reshape(-1,1)#必须转换成一维的数组，否则会报错，reshape(-1,1)若干行一列

#模型预测（第一次尝试用线性回归模型）
from sklearn.linear_model import  LinearRegression
lr1 = LinearRegression()#创建lr1训练模型
lr1.fit(X_train,y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

#加载测试数据集
data_test = pd.read_csv('testValue.csv')
X_test = data_test.loc[:,'T']
y_test = data_test.loc[:,'R']

X_test = np.array(X_test).reshape(-1 ,1)
#用测试数据集预测
y_train_predict = lr1.predict(X_train)
y_test_predict = lr1.predict(X_test)

from sklearn.metrics import r2_score  #R2决定系数（拟合优度）模型越好：r2->1 模型越差：r2->0
r2_train = r2_score(y_train,y_train_predict)
r2_test = r2_score(y_test,y_test_predict)
print('training r2:',r2_train)
print('test r2:',r2_test)
#可明显看出训练效果很差
#训练结果可视化--可以看出线性模型不使用当前情况
X_range = np.linspace(16,22,300).reshape(-1,1)
y_range_predict = lr1.predict(X_range)

fig2 = plt.figure(figsize=(5,5))
plt.plot(X_range,y_range_predict)
plt.scatter(X_train,y_train)

plt.title('prediction data')
plt.xlabel('temperature')
plt.ylabel('rate')
plt.show()