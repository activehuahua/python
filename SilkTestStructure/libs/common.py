# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 14:12
# @Author  : zhaojianghua
# @File    : common.py
# @Software: PyCharm
# @Desc    :
from data import  api_front_catalogproducts_data
class Common():
    def get_parameter(self):
        list= api_front_catalogproducts_data._CATALOG_PRODUCT_DETAIL
        param_list=[]
        for item in range(len(list)):
             param_list.append(list[item]['variant_sku'])
        print(param_list)
        return  param_list