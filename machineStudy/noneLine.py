
# -*- coding: utf-8 -*-#

'''
# Name:         noneLine
# Description:  
# Author:       alex
# Date:         2022/7/7
'''
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#生成如下数据集
a= np.arange(1,16)
b=np.array([74.9,74.5,74.95,75.2,75.2,74.4,74.8,74.85,74.35,74.25,74.25,74.3,74,74.25,74.35])
data = np.c_[a,b]

#给x,y分别添加维度
x = data[:,0,np.newaxis]
y=data[:,1,np.newaxis]
plt.scatter(x,y)
plt.show()

def multi_feature(x,n):
    c = np.empty((x.shape[0],0)) #np.empty((3,1))并不会生成一个3行1列的空数组,np.empty((3,0))才会生成3行1列空数组
    for i in range(n+1):
        h=x**i
        c=np.c_[c,h]
    return c

#先设置n=2
x_1 = multi_feature(x,5)
#用新生成的x作为输入


class normal():
    def __init__(self):
        pass

    def fit(self, x, y):
        # x_1中已经生成了一列1，不需要再加偏置，因此注释掉这2列。

        # m=x.shape[0]
        # X = np.concatenate((np.ones((m,1)),x),axis=1)
        xMat = np.mat(x)
        yMat = yMat = np.mat(y.reshape(-1, 1))

        xTx = xMat.T * xMat
        # xTx.I为xTx的逆矩阵
        ws = xTx.I * xMat.T * yMat
        return ws


model = normal()
# 用新生成的x作为输入
w = model.fit(x_1, y)

#计算x_1的拟合效果，下面是矩阵乘法
y_1 = np.dot(x_1,w)

ax1= plt.subplot()
ax1.plot(x,y_1,c='r',label='n=5时，拟合效果图')
ax1.scatter(x,y,c='b',label='真实分布图')
ax1.legend(prop = {'size':15}) #此参数改变标签字号的大小
plt.show()

x_test = np.linspace(1,22,100)
x_3 = multi_feature(x_test,5)

#生成预测值y_3
y_3 = np.dot(x_3,w)
ax1= plt.subplot()
ax1.plot(x_test,y_3,c='r',label='n=5时，拟合效果图')
ax1.scatter(x,y,c='b',label='真实分布图')
ax1.legend(prop = {'size':15}) #此参数改变标签字号的大小
plt.show()

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_1, y)
print('截距为：',model.intercept_,'\n')
print('系数为：',model.coef_,'\n')
print(w)
