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
from readExcel import ReadExcel
import os,json
from time import sleep
from selenium import webdriver
#import excelunit

testData=ReadExcel.readExcel("login.xlsx","Sheet1")

# data=excelunit.ExcelUtil("login.xlsx","Sheet1")
# testData=data.dict_data()
#testData=dict(testData)
#testData=json.dump(testData)
print(testData)
#testData=data.dict_data()

browser = webdriver.Chrome()
browser.maximize_window()

@ddt
class Test1(unittest.TestCase):
    def setUp(self):

        username = "hmuat"  # stands for !@user
        password = "go4uat"  # stands for ^&pass
        url = 'ec.qingmutec.com'
        webUrl = 'https://{}:{}@{}'.format(username, password, url)
        browser.get(webUrl)

    def tearDown(self):
        pass

    @data(*testData)
    def test_login(self,data):
        print ("当前测试数据%s" % data)
        login_url = 'https://ec.qingmutec.com/en_cn/customer/account/login/'
        browser.get(login_url)
        email =browser.find_element_by_id('email')
        password =browser.find_element_by_id('pass')

        email.send_keys(data['phone'])
        password.send_keys(data['password'])
        print(data['phone'])
        login = browser.find_element_by_id('send2')
        login.click()
        sleep(3)
        loginResult =browser.find_element_by_xpath(
            '//div[@class="session-menu"]/ul/a/li[@class="user-regs  login_act "]/span')
        print(email)
        expectResult=data['expect_txt']
        print (expectResult)

        self.assertEqual(loginResult.text,expectResult)

if __name__ == '__main__':
    unittest.main()