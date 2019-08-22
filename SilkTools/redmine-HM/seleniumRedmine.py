#!/usr/bin/python3
# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import re, string
import config as CF


class SeleniumRedmine(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(CF.base_url)

        self.driver.find_element_by_id('username').send_keys('alexander.zhao')
        self.driver.find_element_by_id('password').send_keys('Mi123456')
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
       # self.driver.get(CF.uat_url)

    def getEachNumber(self):
        for key in CF.UATData:
            self.driver.get(CF.UATData[key])
            number = self.driver.find_element_by_xpath('//p[@class="pagination"]/span[@class="items"]').text
            print(key, self.getNumber(number))

    def getAppEachNumber(self):
        for key in CF.AppData:
            self.driver.get(CF.AppData[key])
            try:
                number = self.driver.find_element_by_xpath('//p[@class="pagination"]/span[@class="items"]').text
                print(key, self.getNumber(number))
            except:
                pass

    def getNumber(self,content):
        number = content.split('/')[1]
        number = number.replace(')', '')
        return number

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    redmine = SeleniumRedmine()
    redmine.getEachNumber()
    print('***********************************')
    redmine.getAppEachNumber()
    redmine.quit()
