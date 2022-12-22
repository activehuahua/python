# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 10:44
# @Author  : zhaojianghua
# @File    : githublogin.py
# @Software: PyCharm
# @Desc    :

import requests
from lxml import etree
import time
from pyquery import PyQuery as pq

class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers )
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')
        if token:
            self.token=token[1]  #此处原来是0，改为1后代码可用
        print(self.token)
        #return token

    def login(self, acount, password):
        self.token()
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token,
            'login': acount,
            'password': password
        }
        #print(post_data)
        response = self.session.post(self.post_url, data=post_data, headers=self.headers )
        result=response.text
        #print(result)
        #print(response.text)
        # if response.status_code == 200:
        #     self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        time.sleep(3)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        for item in dynamics:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self, html):
        selector = etree.HTML(html)
        #name = selector.xpath('//input[@id="user_profile_name"]/@value')
        name = selector.xpath('//*[@id="user_profile_name"]/@value')
        #email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name)

        doc = pq(html)
        page_title = doc("title").text()
        user_profile_bio = doc("#user_profile_bio").text()
        user_profile_name = doc("#user_profile_name").attr("value")
        user_profile_location = doc("#user_profile_location").attr("value")
        print(f"页面标题：{page_title}")
        print(f"name：{user_profile_name}")


if __name__ == "__main__":
    login = Login()
    login.login(acount='activehuahua', password='Cdzjh730815')
