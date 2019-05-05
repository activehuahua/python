# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 15:00
# @Author  : zhaojianghua
# @File    : test_api_company.py
# @Software: PyCharm
# @Desc    :

from API_GetCompany import API_GetCompany
import api_company_data
import json
#import pytest

class Test_API_Company():


    api_company=API_GetCompany()
    param=api_company_data._params
    api_company.set_param(param)
    api_company.header=api_company_data._headers
    content=api_company.get_catalog_compang()
    print(content)

    def test_company_count(self):
        print(self.content)
        Json=json.loads(self.content)
        count=len(Json['companylist'])
        assert  count ==33

    # @pytest.mark.parametrize('content', content)
    # def test_catalog_count(self,content):
    #     Json = json.loads(content)
    #     count = len(Json['catalogs'])
    #     assert count==11

    # @pytest.mark.parametrize('content', content)
    # def test_company_info(self,content):
    #     Json = json.loads(content)
    #     id=api_company_data._bruce_company['id']
    #     for item in range(len(Json['companylist'])):
    #         if Json['companylist']['id']==id:
    #             assert Json['companylist']['companyName'] =='Bruce Test Admin'
    #             assert Json['companylist']['catalog_name'] == 'Bruce TEST Update'
    #             assert Json['companylist']['phone'] == '13800138000'
    #             assert Json['companylist']['email'] == 'brucehuang@silk.com'
    #         else:
    #             continue
    #
    # @pytest.mark.parametrize('content', content)
    # def test_catalog_info(self,content):
    #     Json = json.loads(content)
    #     id = api_company_data._catalog_data['id']
    #     for item in range(len(Json['catalog'])):
    #         if Json['catalog']['id'] == id:
    #             assert Json['catalog']['catalog_description'] == 'Sylvia Catalog'
    #             assert Json['catalog']['catalog_name'] == 'Sylvia Catalog'
    #             assert Json['catalog']['root_catalog_id'] == '1872565557039665640'
    #             assert Json['catalog']['store_hash'] == 'h3jnjw30qw'
    #             assert Json['catalog']['created_date'] == '2018-12-04 18:22:27'
    #
    #         else:
    #             continue


# if __name__ == '__main__':
#     testAPICompany=Test_API_Company()
#     api_company=API_GetCompany()
#     param=api_company_data._params
#     api_company.set_param(param)
#     api_company.header=api_company_data._headers
#     content=api_company.get_catalog_compang()
#     print(content)
#
#     testAPICompany.test_company_count()