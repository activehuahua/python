# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 17:05
# @Author  : zhaojianghua
# @File    : login.py
# @Software: PyCharm
# @Desc    :

from selenium import  webdriver
from selenium.webdriver.common.by import By
from initBase import baseClass

class loginHMF(baseClass):


    def loginKLFActions(self):
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys("18920003001")
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")

        #driver.find_element_by_xpath("//button").click()
        #driver.find_element_by_xpath("//button[@class='el-button aw el-button--primary']").click()
        #driver.find_element_by_css_selector('[class="el-button aw el-button--primary"]').click()
        self.driver.find_element_by_css_selector('.el-button.aw.el-button--primary').click()
        return self.driver

    def loginHMFActions(self):
        accout=self.driver.find_element_by_id('account')
        password=self.driver.find_element_by_id('password')
        loginButton=self.driver.find_element_by_id('loginBtn')
        accout.clear()
        password.clear()
        accout.send_keys('ccadmin')
        password.send_keys('qazwsx1')
        loginButton.click()
        return self.driver

