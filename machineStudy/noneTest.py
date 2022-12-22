
# -*- coding: utf-8 -*-#

'''
# Name:         noneTest
# Description:  
# Author:       alex
# Date:         2022/7/8
'''
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# 训练集
y = [.27, .16, .06, .036, .044, .04, .022, .017, .022, .014, .017, .02, .019, .017, .011, .01, .03, .05, .066, .09]
x = list(range(len(y)))
# 待测集
n = 200
w = [i/n*len(y) for i in range(n)]

# 建模
model = Sequential()
model.add(Dense(units=10, input_dim=1, activation='sigmoid'))
model.add(Dense(units=1, activation='sigmoid'))
# 编译、优化
model.compile(optimizer=Adam(), loss='mse')

for i in range(10):
    # 训练
    model.fit(x, y, epochs=2500, verbose=0)
    print(i, 'loss', model.evaluate(x, y, verbose=0))
    # 预测
    z = model.predict(w)
    # 可视化
    pyplot.subplot(2, 5, i + 1)
    pyplot.xticks(())
    pyplot.yticks(())
    pyplot.scatter(x, y)  # 样本点
    pyplot.scatter(w, z, s=2)  # 预测线
pyplot.show()
