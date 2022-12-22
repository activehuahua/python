# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:27
# @Author  : zhaojianghua
# @File    : LoginPage.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from hm_pages.po_module import Page

class LoginPage(Page):

    email_loc=(By.ID,"email")
    password_loc=(By.ID,"pass")
    loginResult_loc=(By.XPATH,"//div[@class='session-menu']/ul/a/li[@class='user-regs  login_act ']/span")
    login_loc=(By.ID,"send2")


    #Action
    def type_email(self,email):
        self.find_element(*self.email_loc).send_keys(email)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.login_loc).click()

    def getAccoutName(self):
        '''获取email值'''
        return self.find_element(*self.accoutName_loc).get_attribute('value')

    '''获取登录错误提示'''
    def getErrorMessage(self):
        return self.find_element(*self.errormessage_loc).text

    def getText(self):
        return self.find_element(*self.loginResult_loc).text

    def user_login(self,username,password):
        url='/en_cn/customer/account/login/'
        self._open(url)
        self.type_email(username)
        self.type_password(password)
        self.submit()
