# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 16:32
# @Author  : zhaojianghua
# @File    : 0.py
# @Software: PyCharm
# @Desc    :

# -*- coding: UTF-8 -*-
import pandas as pd
df = pd.DataFrame([{'col1':'a', 'col2':'1'}, {'col1':'b', 'col2':'2'}])

print(df.dtypes)

df['col2'] = df['col2'].astype('int')
print('-----------')
print(df.dtypes)

df['col2'] = df['col2'].astype('float64')
print('-----------')
print(df.dtypes)
