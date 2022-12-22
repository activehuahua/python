# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:20
# @Author  : zhaojianghua
# @File    : po_module.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from config import configs

class Page(object):
    _instance = None
    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Page, "_instance"):
            cls._instance = cls(*args, **kwargs)
        return cls._instance

    def __init__(self):
        self.base_url=configs.BaseURL

        self.base_url = 'https://{}:{}@{}'.format(configs.authName, configs.authPwd, configs._URL)
        # if self._instance is None:
        #     self.driver = webdriver.Chrome()
        #     #self.driver=driver
        #     self.driver.implicitly_wait(30)
        #     self.driver.maximize_window()
        #     self.instance()

        self.driver = webdriver.Chrome()

        #self.driver=driver
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
