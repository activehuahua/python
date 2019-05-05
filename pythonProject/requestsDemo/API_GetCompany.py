# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 22:02
# @Author  : zhaojianghua
# @File    : API_GetCompany.py
# @Software: PyCharm
# @Desc    :

from api_backend_module import API_BackEnd_Page
import configs
import requests
import json
import string
from time import sleep

class API_GetCompany(API_BackEnd_Page):
    '''APP的链接地址'''
    app_url=configs._URL+configs.APP_URL

    '''company接口地址'''
    api_url=configs._API_Backend_URL+'/api/companies'

    def get_catalog_compang(self):
       # api_getCompany=API_GetCompany()

       s=requests.Session()
       login_url=configs.LOGIN_URL

       r=s.post(login_url,headers=self.header,params=self.params)
       sleep(3)

       r1 = s.get(self.app_url, headers=self.header)

       cookies = r1.cookies.get_dict()

       r2 = s.get(self.api_url, headers=self.header, cookies=cookies)

       print(r2.text)
       content=str(r2.text)
       return content