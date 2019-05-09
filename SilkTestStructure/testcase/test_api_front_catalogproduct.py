# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 18:06
# @Author  : zhaojianghua
# @File    : test_api_front_catalogproduct.py
# @Software: PyCharm
# @Desc    : 测试前台catalog products接口
from b2b_api.api_front_getcatalogproducts import API_Front_GetCatalogProducts
from data import api_front_catalogproducts_data as apidata
import json
import pytest
from libs.common import  Common

class Test_API_Front_CatalogProducts():
    def setup(self):
        api_catalogProduct=API_Front_GetCatalogProducts()
        param=apidata._COMPANY_ID
        api_catalogProduct.set_param(param)
        api_catalogProduct.header=apidata._Headers
        self.content=api_catalogProduct.get_catalog_products()
        # self.paramList=self.get_parameter()


    def get_detail_item(self):
        Json = json.loads(self.content)
        sku = apidata._CATALOG_PRODUCT_DETAIL['variant_sku']
        for item in range(len(Json)):
            if Json[item]['variant_sku'] == sku:
                return Json[item]
            else:
                continue


    def get_parameter(self):
        list=apidata._CATALOG_PRODUCT_DETAIL
        param_list=[]
        for item in range(len(list)):
             param_list.append(list[item]['variant_sku'])
        print(param_list)
        return  param_list


    def test_catalog_products_count(self):
        '''
        判断catalog products总数的用例
        '''
        Json = json.loads(self.content)
        assert len(Json) ==37


    def test_catalog_product_detail_single(self):
        '''判断具体的Product 详细信息是否正确'''
        Json = json.loads(self.content)
        sku=apidata._CATALOG_PRODUCT_DETAIL_Single['variant_sku']
        for item in range(len(Json)):
            if Json[item]['variant_sku']==sku:
                # print('price=',Json[item]['tier_price'][0]['price'])
                assert Json[item]['company_catalog_id']==apidata._CATALOG_PRODUCT_DETAIL_Single['company_catalog_id']
                assert Json[item]['store_hash']==apidata._CATALOG_PRODUCT_DETAIL_Single['store_hash']
                assert Json[item]['variant_id'] == apidata._CATALOG_PRODUCT_DETAIL_Single['variant_id']
                assert Json[item]['id'] == apidata._CATALOG_PRODUCT_DETAIL_Single['id']
                assert Json[item]['product_id'] == apidata._CATALOG_PRODUCT_DETAIL_Single['product_id']
                assert Json[item]['tier_price'][0]['price'] == apidata._CATALOG_PRODUCT_DETAIL_Single['price']
                assert Json[item]['tier_price'][0]['type'] == apidata._CATALOG_PRODUCT_DETAIL_Single[
                    'type']
                assert Json[item]['tier_price'][0]['qty'] == apidata._CATALOG_PRODUCT_DETAIL_Single[
                    'qty']
            else:
                continue


    # params=['SKU079','SKU081']
    common=Common()
    params=common.get_parameter()

    @pytest.mark.parametrize('sku', params)
    def test_catalog_products_detail(self,sku):
        '''设置参数，进行多次运行'''
        Json = json.loads(self.content)
        print('sku=',sku)
        #sku = api_front_catalogproducts_data._CATALOG_PRODUCT_DETAIL_Single['variant_sku']
        datalist=apidata._CATALOG_PRODUCT_DETAIL
        data_sku_pos =-1
        for pos in range(len(datalist)):
            if datalist[pos]['variant_sku']==sku:
                data_sku_pos=pos
                print(data_sku_pos)

        for item in range(len(Json)):
            if Json[item]['variant_sku'] == sku:
                # print('price=',Json[item]['tier_price'][0]['price'])
                assert Json[item]['company_catalog_id'] == \
                       apidata._CATALOG_PRODUCT_DETAIL[data_sku_pos]['company_catalog_id']
                assert Json[item]['store_hash'] == apidata._CATALOG_PRODUCT_DETAIL[data_sku_pos]['store_hash']
                assert Json[item]['variant_id'] == apidata._CATALOG_PRODUCT_DETAIL[data_sku_pos]['variant_id']
                assert Json[item]['id'] == apidata._CATALOG_PRODUCT_DETAIL[data_sku_pos]['id']
                assert Json[item]['product_id'] == apidata._CATALOG_PRODUCT_DETAIL[data_sku_pos]['product_id']
                assert Json[item]['tier_price'][0]['price'] == apidata._CATALOG_PRODUCT_DETAIL[data_sku_pos]['price']
                assert Json[item]['tier_price'][0]['type'] ==apidata._CATALOG_PRODUCT_DETAIL[data_sku_pos]['type']
                assert Json[item]['tier_price'][0]['qty'] == apidata._CATALOG_PRODUCT_DETAIL[data_sku_pos]['qty']
            else:
                continue