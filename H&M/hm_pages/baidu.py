# coding=utf-8
'''
Created on 2016-7-22
@author: Jennifer
Project:登录百度测试用例
'''
from selenium import webdriver
import unittest, time

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from hm_pages import LoginPage
from time import sleep
from config import  configs
import unittest
import ddt

from hm_pages.po_module import Page
from libs.readExcel import ReadExcel
base_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data\login.xlsx')
print(base_path)


testData=ReadExcel.readExcel(r"{0}".format(base_path), "Sheet1")
print(testData)

@ddt.ddt
class HMLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒

        #self.base_url = "https://www.baidu.com"

    # def test_baidu(self):
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     driver.find_element_by_id("kw").clear()
    #     driver.find_element_by_id("kw").send_keys("unittest")
    #     driver.find_element_by_id("su").click()
    #     time.sleep(3)
    #     title = driver.title
    #     self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*testData)
    def test_login(self, data):
        driver=self.driver
        print("当前测试数据%s" % data)
        print(data['phone'],data['password'])

        print(self.driver)
        loginClass=LoginPage.LoginPage(driver)

        loginClass.user_login(data['phone'],data['password'])
        sleep(3)
        loginResult = loginClass.getText()

        expectResult = data['expect_txt']
        print(expectResult)

        self.assertEqual(loginResult, expectResult)
if __name__ == "__main__":
    #unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(BaiduTest)
    unittest.TextTestRunner().run(suite)