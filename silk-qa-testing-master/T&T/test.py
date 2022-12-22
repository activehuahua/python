from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("www.baidu.com")
# a=driver.find_element_by_name('send').is_displayed()
# print(type(a))
# sleep(4)
# # driver.find_element_by_xpath('//*[@class="col-5"]/div/ol/li[1]/div/div[1]/div/div[2]/div/div/form/button').click()
# # sleep(3)
# # aaa=driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/div/div/div').text
# # print(aaa)