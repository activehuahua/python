#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : headless-ep.py
@Time    : 2018/12/7 13:27
@desc   :
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    #添加代理选项
    #chrome_options.add_argument('--proxy-server=http://'+proxy)

    # chrome_options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get("https://www.qiushibaike.com/8hr/page/1/")
    print(driver.page_source)
    driver.close()


if __name__ == '__main__':
    main()
