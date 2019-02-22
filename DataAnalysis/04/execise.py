# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 11:46
# @Author  : zhaojianghua
# @File    : execise.py
# @Software: PyCharm
# @Desc    :

import  numpy as np
import sys




scoreType=np.dtype({
    'names':['name','Chinese','English','Math','Total'],
    'formats':['U32','i','i','i','i']})

scores=np.array(
    [("张飞",66,65,30,0),("关羽",95,85,98,0),("赵云",93,92,96,0),
     ("黄忠",90,88,77,0),("典韦",80,90,90,0)],dtype=scoreType)

chinese=scores[:]['Chinese']
english=scores[:]['English']
math=scores[:]['Math']
scores[:]['Total']=scores[:]['Chinese']+scores[:]['English']+scores[:]['Math']

for col in scores.dtype.names:
    if col =='name' or col == 'Total' :
        continue
    print ("mean of {}:{}".format(col,np.mean(scores[:][col])))
    print ("amax of {}:{}".format(col,np.amax(scores[:][col])))
    print ("amin of {}:{}".format(col,np.amin(scores[:][col])))
    print ("std of {}:{}".format(col,np.std(scores[:][col])))
    print ("var of {}:{}".format(col,np.var(scores[:][col])))

# print(f'[语文]:平均成绩是：{np.mean(chinese)},最小成绩:{np.amin(chinese)}，最大成绩:{np.amax(chinese)}，方差:{np.var(chinese)}，标准差:{np.std(chinese)}')
#
# print(f'[英语]:平均成绩是：{np.mean(english)},最小成绩:{np.amin(english)}，最大成绩:{np.amax(english)}，方差:{np.var(english)}，标准差:{np.std(english)}')
#
# print(f'[数学]:平均成绩是：{np.mean(math)},最小成绩:{np.amin(math)}，最大成绩:{np.amax(math)}，方差:{np.var(math)}，标准差:{np.std(math)}')

print("排名:")
print(np.sort(scores,order='Total'))

ranking = sorted(scores, key=lambda x: x[1] + x[2] + x[3], reverse=True)
print(ranking)

ranking = sorted(scores, key=lambda x: x[4], reverse=True)
print(ranking)