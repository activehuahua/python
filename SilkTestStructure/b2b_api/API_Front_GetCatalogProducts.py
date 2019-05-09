# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 9:28
# @Author  : zhaojianghua
# @File    : API_Front_GetCatalogProducts.py
# @Software: PyCharm
# @Desc    :前台获取 catalog products

from b2b_api.api_front_module import API_Front_Page
from config import configs
import requests
import json
import string
from time import sleep

class API_Front_GetCatalogProducts(API_Front_Page):


    url='/prod/catalogproducts'

    def get_catalog_products(self):

       content=self.get_html(self.url)

       return content