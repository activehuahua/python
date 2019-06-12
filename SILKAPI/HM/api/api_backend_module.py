# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 17:20
# @Author  : zhaojianghua
# @File    : po_module.py
# @Software: PyCharm
# @Desc    :
# import sys
# sys.path.append("./config")
import requests,json,re
from time import sleep
from config import configs

class API_BackEnd_Page(object):


    def __init__(self):
        self.header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
        self.base_url=configs._API_Backend_URL
        self.params={}
        self.header={}

    '''设置参数'''
    def set_param(self,params):
        self.params=params

    '''获取返回文本'''
    def get_html(self,url):
        r=requests.get(self.base_url+url,headers=self.header,params=self.params)
        html = r.text
        return html

    '''获取匹配的数据集'''
    def get_matches(self,html,re_pattern):
        pattern = re.compile(re_pattern)
        lists = []
        finds = re.findall(pattern, html)
        for item in finds:
            lists.append(lists + item)
        return lists

    '''获取结果数'''
    def get_json_count(self,html):
         Json = json.loads(html)
         return len(Json)