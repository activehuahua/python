# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 16:15
# @Author  : zhaojianghua
# @File    : new_count.py
# @Software: PyCharm
# @Desc    :
from count import A

class B(A):
    def sub(self,a,b):
        return a-b

result=B().add(2,5)
print(result)