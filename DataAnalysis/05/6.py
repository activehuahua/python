# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 16:58
# @Author  : zhaojianghua
# @File    : 6.py
# @Software: PyCharm
# @Desc    :SQL方式查询数据

import pandas as pd
from pandas import DataFrame
from pandasql import sqldf
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='a'"
print(pysqldf(sql))
