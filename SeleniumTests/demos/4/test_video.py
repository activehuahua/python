# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 15:29
# @Author  : zhaojianghua
# @File    : test_video.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://videojs.com/")
driver.implicitly_wait(10)

video=driver.find_element_by_id('preview-player_html5_api')
#video=driver.find_element_by_xpath("body/section[0]/div/video")

url=driver.execute_script("return arguments[0].currentSrc;",video)

print(url)

print('start')
driver.execute_script("return arguments[0].play()",video)

sleep(3)

print('stop')
driver.execute_script("arguments[0].pause()",video)

driver.get_screenshot_as_file("video.png")

#driver.quit()