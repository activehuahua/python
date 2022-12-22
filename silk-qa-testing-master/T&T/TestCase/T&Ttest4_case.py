import unittest,random,sys,os
from time import sleep
from ddt import ddt,data,unpack
from page_object.gowuc import gwc
from model import myunit
from model.operationExcel import ReadExcel

@ddt
class addcartTest(myunit.MyTest):
    '''商品加入购物车测试用例'''
    @data(*ReadExcel.readExcels("gouwuc.xlsx","商品加入购物车"))
    def test_addcart1(self, data):
        ''' 首页商品加入到购物车'''
        po = gwc(self.driver)
        po.addcar_Action(**data)
        '''断言首页加入商品提示语'''
        self.assertEqual(data['expect_txt'], po.car_meaasge())

if __name__ == "__main__":
     unittest.main()