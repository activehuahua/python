#!/usr/bin/python3
# -*-coding:utf-8 -*-

import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

class redmine(object):
    def __init__(self):
        self.base_url='https://redmine.silksoftware.com/login?back_url=https%3A%2F%2Fredmine.silksoftware.com%2F'
        self.login_url='https://redmine.silksoftware.com/login'
        self.domain='https://redmine.silksoftware.com/'

        self.user_name='alexander.zhao'
        self.password='Mi123456'
        self.session = requests.Session()
        self.headers = {
            'Referer': 'https://redmine.silksoftware.com/login?back_url=https%3A%2F%2Fredmine.silksoftware.com%2F',
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'silksoftware.com',
            'Cookie':'_redmine_session=ZmdaS1VhY21jd0VzczRzS2FxME16M1FTVGlkb205Qy9xVzFTVFdMak92MVZ3Z3RlQ0I2VXlBaGd0YXVhSlF4ZHdVQnBpekZEUE0wb1Mxa3FzWjdiS1o0KytaRm80M3k4Z1Ria1ltZHdDNjIvZk9JVDZpQTNXYzRMOTlvMzlKbTA0UUhJOFZ4YnZ6VHhOSUlsY1hnd3hSdytzTmdydEphNy82dUhrYTJsR2RpOUFxZFpDbHp2YXE0a2FrY24rK1pGLS15NkRjWUV5d2kzZ2pOUGpqMlYzN29RPT0%3D--f7d484d0e9b1e8691bcfc64a51b7d99d0393935f'
        }
        self.login_params={}

    def set_login_params(self):
        token2=self.token()
        self.login_params = {
            "utf8":"✓",
            "login":"登录 »",
            "username": "alexander.zhao",
            "password": "Mi123456",
            "back_url": "https://redmine.silksoftware.com/",
            "authenticity_token":token2
        }
    def login(self):
        self.set_login_params()
        print(self.login_params)
        r=self.session.post(self.login_url,data=self.login_params, headers=self.headers,verify=False)

        #r=self.session.get(self.domain,headers=self.headers,verify=False)  ,allow_redirects=False

        print(r.text)

    def token(self):
        response=self.session.get(self.base_url,verify=False)
        doc=pq(response.text)
        token1=doc('meta[name="csrf-token"]').attr("content").strip()
        token2 = doc('Input[name="authenticity_token"]').attr("value").strip()
        print(token1,token2)
        return  token1

if __name__ == '__main__':
    Redmine_HM=redmine()
    Redmine_HM.login()