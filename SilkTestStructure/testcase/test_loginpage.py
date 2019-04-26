# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:42
# @Author  : zhaojianghua
# @File    : test_loginpage.py
# @Software: PyCharm
# @Desc    :
from SilkTestStructure.pages  import LoginPage
#import pytest
from time import sleep
from SilkTestStructure.config  import configs
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_loginPage():

    driver=webdriver.Chrome()

    def test_login1(self):
        username=configs._SCLOGIN['username']
        password=configs._SCLOGIN['password']

        LoginPage.user_login(self,username,password)
        sleep(3)
        accountName=self.driver.find_element_by_xpath("//div[contains(@class,'text-right') and contains(@class,'admin-desc')]/a").text
       # assert accountName=='fdfdfd'

    if __name__ == '__main__':
        test_login1()