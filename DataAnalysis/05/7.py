# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 18:03
# @Author  : zhaojianghua
# @File    : 7.py
# @Software: PyCharm
# @Desc    :

import pandas as pd
import numpy as np
from pandas import DataFrame

df=pd.DataFrame(np.random.random([3, 3]),
     columns=['A', 'B', 'C'], index=['first', 'second', 'third'])
print(df)

print(df.round(2))

print(df.round({'A':2}))