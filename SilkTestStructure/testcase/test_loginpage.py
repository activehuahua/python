# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:42
# @Author  : zhaojianghua
# @File    : test_loginpage.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.by import By
# import sys
# sys.path.append("./data")
# sys.path.append("./b2b_pages")
from b2b_pages import LoginPage
#import pytest
from time import sleep
from config import  configs
from data import login_data


class Test_loginPage():
    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver=webdriver.Chrome(options=option)
        #self.driver = webdriver.Chrome()
        # driver.implicitly_wait(30)

    '''错误用户名和密码登录'''

    def test_errorLogin(self):
        username = login_data._errorLoginData1['username']
        password = login_data._errorLoginData1['password']

        loginPage = LoginPage.LoginPage(self.driver)
        loginPage.user_login(username, password)
        sleep(3)
        errorInfo = loginPage.getErrorMessage()
        assert 'Your email address or password is incorrect.' in errorInfo


    '''正确用户名和密码登录'''
    def test_login1(self):
        username=login_data._admin['username']
        password=login_data._admin['password']

        loginPage=LoginPage.LoginPage(self.driver)
        loginPage.user_login(username,password)

        sleep(3)
        accountName=loginPage.getAccoutName()

        print(accountName)
        assert accountName==username

    def teardown(self):
        self.driver.quit()

