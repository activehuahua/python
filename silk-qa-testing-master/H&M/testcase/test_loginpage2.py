# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:42
# @Author  : zhaojianghua
# @File    : test_loginpage.py
# @Software: PyCharm
# @Desc    :
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from hm_pages import LoginPage
from time import sleep
from config import  configs
import unittest
from ddt import ddt,data,unpack

from hm_pages.po_module import Page
from libs.readExcel import ReadExcel
base_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data\login.xlsx')
print(base_path)


testData=ReadExcel.readExcel(r"{0}".format(base_path), "Sheet1")
print(testData)
#driver = webdriver.Chrome()
@ddt
class HMloginPageTest(unittest.TestCase):

    loginClass = LoginPage.LoginPage()
    # def setUp(self):
    #     login_class=self.loginClass
    #     self.driver=self.loginClass.driver

    @classmethod
    def setUpClass(self):
        login_class = self.loginClass
        self.driver = self.loginClass.driver


    @data(*testData)
    def test_login(self, data):
        print("当前测试数据%s" % data)
        print(data['phone'],data['password'])


        self.loginClass.user_login(data['phone'],data['password'])
        sleep(3)
        loginResult = self.loginClass.getText()

        expectResult = data['expect_txt']
        print(expectResult)

        self.assertEqual(loginResult, expectResult)

    @classmethod
    def tearDownClass(self):
        print(11111111111111111)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

