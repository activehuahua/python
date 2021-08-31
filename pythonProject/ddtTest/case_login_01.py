#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : case_login_01.py
@Time    : 2019/8/13 11:16
@desc   :
'''

import unittest
import requests
from ddt import ddt,data,unpack
from ddtTest.readExcel import ReadExcel
import os,json
from time import sleep
from selenium import webdriver
#import excelunit

testData=ReadExcel.readExcel("login.xlsx","Sheet1")
print(testData)

@ddt
class MyTest1(unittest.TestCase):
    def setUp(self):

        self.username = "hmuat"  # stands for !@user
        self.password = "go4uat"  # stands for ^&pass

        self.driver=webdriver.Chrome();
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


    @data(*testData)
    def test_login(self,data):
        browser=self.driver
        print ("当前测试数据%s" % data)
        login_url = 'https://ec.qingmutec.com/en_cn/customer/account/login/'
        login_url = 'https://{}:{}@{}'.format(self.username, self.password, "ec.qingmutec.com/en_cn/customer/account/login/")

        browser.get(login_url)
        closeButton=browser.find_element_by_class_name('action-close')
        closeButton.click()

        email =browser.find_element_by_id('email')
        password =browser.find_element_by_id('pass')

        email.send_keys(data['email'])
        password.send_keys(data['password'])
        print(data['email'])
        login = browser.find_element_by_id('send2')
        login.click()
        sleep(3)
        loginResult =browser.find_element_by_class_name('user-sign')
        print(email)
        expectResult=data['expect_txt']
        print(expectResult)

        self.assertEqual(loginResult.text,expectResult)


if __name__ == '__main__':
    unittest.main()