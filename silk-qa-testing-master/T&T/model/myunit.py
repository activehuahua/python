import unittest
from.driver import browser

from selenium import webdriver
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        # self.driver=driver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.verificationErrors=[]
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cls.assertEqual([],cls.verificationErrors)


