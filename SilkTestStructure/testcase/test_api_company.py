# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 15:00
# @Author  : zhaojianghua
# @File    : test_api_company.py
# @Software: PyCharm
# @Desc    :
# import sys
# sys.path.append("./b2b_api")
# sys.path.append("./data")
from b2b_api.API_GetCompany import API_GetCompany
from data  import api_company_data
import json
import pytest

class Test_API_Company():


    api_company=API_GetCompany()
    param=api_company_data._params
    api_company.set_param(param)
    api_company.header=api_company_data._headers
    content=api_company.get_catalog_compang()
    #print(content)

    '''验证接口公司数量'''
    def test_company_count(self):
        #print(self.content)
        Json=json.loads(self.content)
        count=len(Json['companylist'])
        assert  count ==35

    '''验证接口Catalog数量'''
    def test_catalog_count(self):
        Json = json.loads(self.content)
        count = len(Json['catalogs'])
        assert count==11

    '''验证接口公司详细数据信息'''
    def test_company_info(self):
        Json = json.loads(self.content)
        id=api_company_data._bruce_company['id']
        for item in range(len(Json['companylist'])):
            if Json['companylist'][item]['id']==id:
                assert Json['companylist'][item]['company_name'] =='Bruce Test Admin'
                assert Json['companylist'][item]['catalog_name'] == 'Bruce TEST Update'
                assert Json['companylist'][item]['phone'] == '13800138000'
                assert Json['companylist'][item]['email'] == 'brucehuang@silk.com'
            else:
                continue

    '''验证接口Catalog详细信息'''
    def test_catalog_info(self):
        Json = json.loads(self.content)
        id = api_company_data._catalog_data['id']
        for item in range(len(Json['catalogs'])):
            if Json['catalogs'][item]['id'] == id:
                # assert Json['catalogs'][item]['catalog_description'] == 'Sylvia Catalog'
                # assert Json['catalogs'][item]['catalog_name'] == 'Sylvia Catalog'
                assert Json['catalogs'][item]['root_catalog_id'] == '1872565557039665640'
                assert Json['catalogs'][item]['store_hash'] == 'h3jnjw30qw'
                assert Json['catalogs'][item]['created_date'] == '2018-12-04 18:22:27'

            else:
                continue

