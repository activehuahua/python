# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 17:45
# @Author  : zhaojianghua
# @File    : newHouse.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from login import loginHMF
from initBase import baseClass
import unittest

class newHouse(unittest.TestCase):

    #driver=webdriver.Chrome()
    #login=loginHMF()
    #driver=login.loginHMFActions()
    # def __init__(self):
    #     self.driver=webdriver.Chrome()
    #     self.driver.get("http://partner.fc.igemi.cn")
    #     self.driver.maximize_window()
    def setUp(self):
        print("test start")
        login = loginHMF()
        login.loginHMFActions()
        self.driver=login.driver

    def test_getTotal(self):
        frame=self.driver.find_element_by_xpath("//iframe[@id='house-frame']")
        self.driver.switch_to.frame(frame)
        totalStr=self.driver.find_element_by_xpath("//b[@class='total-count']").text
        self.assertEqual(totalStr,'185')

    def tearDown(self):
        print("test end")

if __name__ == '__main__':

    suit=unittest.TestSuite()
    suit.addTest(newHouse('test_getTotal'))

    runner=unittest.TextTestRunner()
    runner.run(suit)
