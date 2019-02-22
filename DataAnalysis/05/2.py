# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 15:45
# @Author  : zhaojianghua
# @File    : 2.py
# @Software: PyCharm
# @Desc    :

import pandas as pd
from pandas import Series, DataFrame
data = {'Chinese': [66, 95, 93, 90,80],'English': [65, 85, 92, 88, 90],'Math': [30, 98, 96, 77, 90]}
df1= DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
#print(df1)
#print(df2)

#df2.to_excel('data1.xlsx')

df3=DataFrame(pd.read_excel('data1.xlsx'))
print(df3[0:2]['Math'])