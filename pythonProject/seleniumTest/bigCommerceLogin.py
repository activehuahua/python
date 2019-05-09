#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : bigCommerceLogin.py
@Time    : 2019/5/5 9:27
@desc   :
'''

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import re
import requests,json

login_url='https://login.bigcommerce.com/login'
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"'
    #                  ,'Referer:"https://backendappaws.bundleb2b.net/companies"',
    # 'Accept:"application/json, text/plain, */*"',
    # 'Host:"backendappaws.bundleb2b.net"'
                     )
browser = webdriver.Chrome(options=options)

#browser=webdriver.Firefox()
browser.implicitly_wait(10)
browser.get(login_url)

email=browser.find_element_by_id('user_email')
password=browser.find_element_by_id('user_password')
login=browser.find_element_by_xpath('//input[@type="submit"]')

email.send_keys('alexander.zhao@silksoftware.com')
password.send_keys('Silk@123')
login.click()

#sleep(10)

browser.find_element_by_xpath('//div[@id="stores"]/a[2]').click()

api_url='https://backendappaws.bundleb2b.net/api/companies'

header={
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Referer':'https://backendappaws.bundleb2b.net/companies',
    'Accept':'application/json, text/plain, */*',
    'Host':'backendappaws.bundleb2b.net',
    }

# cookies=browser.get_cookies()
#
#
# cookies = {v.get("name"):v.get("value") for v in cookies}
# print(type(cookies),cookies)

# response=requests.get(api_url,headers=header,cookies=cookies)
# #print(response.text)
#
# Json=json.load(response)
#response.json()
#print(type(response),response,response.text)

app=browser.find_element_by_xpath('//div[@id="nav-apps"]')
app.click()

sleep(3)

browser.delete_all_cookies()
browser.refresh()

store_link=browser.find_element_by_xpath('//ul[@class="cp-nav-group-content"]/li/a[@href="/manage/app/13706"]')
store_link.click()

cookies=browser.get_cookies()
cookies = {v.get("name"):v.get("value") for v in cookies}
print(type(cookies),cookies)

response=requests.get(api_url,headers=header,cookies=cookies)
print(response.text)

res=browser.get(api_url)
print(type(res),res)