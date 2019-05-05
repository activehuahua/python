# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:42
# @Author  : zhaojianghua
# @File    : test_loginpage.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages import LoginPage
#import pytest
from time import sleep
from config import  configs
from data import login_data


class Test_loginPage():

    def test_login1(self):
        username=login_data._admin['username']
        password=login_data._admin['password']

        page = LoginPage.LoginPage.user_login(username, password)
        sleep(3)
        accountName=page.getAccoutName()

        print(accountName)
        assert accountName==username

    def test_errorLogin(self):
        username = login_data._errorLoginData1['username']
        password = login_data._errorLoginData1['password']

        page = LoginPage.LoginPage.user_login(username, password)
        sleep(3)
        errorInfo=page.getErrorMessage()
        assert 'Your email address or password is incorrect.' not  in errorInfo

if __name__ == '__main__':
    testLogin=Test_loginPage()
    testLogin.test_login1()
    testLogin.test_errorLogin()