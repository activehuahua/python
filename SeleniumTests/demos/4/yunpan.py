# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 18:58
# @Author  : zhaojianghua
# @File    : yunpan.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

ele1=driver.find_element_by_id('kw')
ActionChains(driver).context_click(ele1).perform()