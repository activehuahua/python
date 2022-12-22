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
    _instance = None
    loginClass = None
    # def setup(self):
    #
    #     self.driver = webdriver.Chrome()
    #     #loginClass=LoginPage.LoginPage(self.driver)
    #
    #     self.driver.implicitly_wait(30)

    @data(*testData)
    def test_login(self, data):
        #driver=self.driver
        print("当前测试数据%s" % data)
        print(data['phone'],data['password'])

        #print(self.driver)
        if HMloginPageTest._instance is None:
            print(11111)
            HMloginPageTest.loginClass=LoginPage.LoginPage()
            HMloginPageTest._instance = '1'

        HMloginPageTest.loginClass.user_login(data['phone'],data['password'])
        sleep(3)
        loginResult = HMloginPageTest.loginClass.getText()

        expectResult = data['expect_txt']
        print(expectResult)

        self.assertEqual(loginResult, expectResult)

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(HMloginPageTest)
    unittest.TextTestRunner().run(suite)
