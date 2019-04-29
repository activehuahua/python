# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:27
# @Author  : zhaojianghua
# @File    : LoginPage.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages.po_module import Page

class LoginPage(Page):

    username_loc=(By.ID,"account")
    password_loc=(By.ID,"password")
    submit_loc=(By.ID,"loginBtn")

    accoutName_loc=(By.XPATH,"//div[contains(@class,'text-right') and contains(@class,'admin-desc')]/a")

    #Action
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

    def getAccoutName(self):
        return self.find_element(*self.accoutName_loc).text


    def user_login(username,password):
        url='/'
        login_page=LoginPage()
        login_page._open(url)
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.submit()
        return login_page
