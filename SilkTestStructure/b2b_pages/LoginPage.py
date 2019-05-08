# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:27
# @Author  : zhaojianghua
# @File    : LoginPage.py
# @Software: PyCharm
# @Desc    :
# import sys
# sys.path.append("./b2b_pages")
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from b2b_pages.po_module import Page

class LoginPage(Page):

    #username_loc=(By.ID,"account")
    username_loc=(By.ID,"login_email")
    password_loc=(By.ID,"login_pass")
    submit_loc=(By.XPATH,"//input[contains(@type,'submit') and contains(@value,'Sign in')]")

    #dashboard 的邮箱地址
    accoutName_loc=(By.ID,"FormField_1_input")

    #账号密码错误提示
    errormessage_loc=(By.XPATH,"//p[@class='alertBox-column alertBox-message']/span")
    #class ="alertBox-column alertBox-message

    #Action
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

    def getAccoutName(self):
        '''获取email值'''
        return self.find_element(*self.accoutName_loc).get_attribute('value')

    '''获取登录错误提示'''
    def getErrorMessage(self):
        return self.find_element(*self.errormessage_loc).text

    # def user_login(username,password):
    #     url='/login.php'
    #     login_page=LoginPage()
    #     login_page._open(url)
    #     login_page.type_username(username)
    #     login_page.type_password(password)
    #     login_page.submit()
    #     return login_page

    def user_login(self,username,password):
        url='/login.php'
        self._open(url)
        self.type_username(username)
        self.type_password(password)
        self.submit()
