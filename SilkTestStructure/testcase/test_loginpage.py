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


class Test_loginPage():

    def test_login1(self):
        username=configs._SCLOGIN['username']
        password=configs._SCLOGIN['password']

        page = LoginPage.LoginPage.user_login(username, password)
        sleep(3)
        accountName=page.getAccoutName()

        print(accountName)
        assert accountName==username

if __name__ == '__main__':
    testLogin=Test_loginPage()
    testLogin.test_login1()