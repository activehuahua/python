# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 10:16
# @Author  : zhaojianghua
# @File    : alertWindow.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)

link=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

driver.find_element_by_link_text('搜索设置').click()
wait=WebDriverWait(driver,5)

button=driver.find_element_by_xpath("//div[@id='gxszButton']/a[@class='prefpanelgo']")

time.sleep(3)
print(button.text)

button.click()


#time.sleep(3)

driver.switch_to.alert.accept()
#driver.quit()