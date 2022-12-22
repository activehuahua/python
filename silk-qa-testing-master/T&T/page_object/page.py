from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from config import configs

class Page(object):
    def __init__(self, driver, base_url =configs.devURL,parent=None):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.parent=parent



    def _open(self, url):
        url= self.base_url+url
        #print(url_)
        # self.driver.maximize_window()
        self.driver.get(url)
        sleep(2)
        # assert self.driver.current_url==url, 'Did ont land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def swtich_window(self,loc):
        return self.driver.switch_to.window(loc)
    #定义script方法，用于执行js脚本
    def script(self,*src):
        self.driver.execute_script(*src)

    #获取当前窗口句柄
    def handle_now(self):
        return self.driver.current_window_handle

    #获取所有窗口
    def handle_all(self):
        return self.driver.window_handles

    #切换窗口
    def handle_switch(self,handle):
        return self.driver.switch_to.window(handle)

