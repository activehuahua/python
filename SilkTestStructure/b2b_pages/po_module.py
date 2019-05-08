# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:20
# @Author  : zhaojianghua
# @File    : po_module.py
# @Software: PyCharm
# @Desc    :
# import sys
# sys.path.append("./config")
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from config import configs

class Page(object):


    def __init__(self,driver):
        self.base_url=configs._URL
        option=webdriver.ChromeOptions()
        option.add_argument('headless')
        # self.driver=webdriver.Chrome(options=option)
        #self.driver = webdriver.Chrome()
        self.driver=driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


    def on_page(self):
        return self.driver.current_url ==(self.base_url+self.url)

    def _open(self,url):
        self.url=self.base_url+url
        self.driver.get(self.url)
        # assert self.on_page(),'Did not land on %s'% self.url

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
