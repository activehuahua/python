# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 11:03
# @Author  : zhaojianghua
# @File    : presale.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver

url='http://www.ccfdw.gov.cn/ecdomain/lpcs/xmInfo.jsp?Id_xmxq=0a56d4be4603439a99fca799171d6fc7&XMMC=%25E5%258D%2593%25E6%2589%25AC%25C2%25B7%25E5%258C%2597%25E6%25B9%2596%25E6%25B9%25BEA%25E5%258C%25BA'

driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame("louListiframe")

loudong_1=driver.find_element_by_xpath('//*[@id="content"]/div[5]/a')
loudong_3=driver.find_element_by_xpath('//*[@id="content"]/div[9]/a')

print(loudong_1.text)
print(loudong_3.text)

loudong_1.click()