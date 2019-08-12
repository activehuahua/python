# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 13:34
# @Author  : zhaojianghua
# @File    : test_mqlength.py
# @Software: PyCharm
# @Desc    :

import requests
from time import sleep
def test_mq():
    url='http://122.112.250.39:15672'
    s=requests.Session()
    r=s.get(url,auth=('crm','crm2019'))

    sleep(10)
    api_url=url+'/api/queues'
    r1=requests.get(api_url, auth=('crm','crm2019'))
    print(r1.url)
    # print(r1.json())
    res = list(map(lambda x:x["backing_queue_status"]["len"], r1.json()))
    print(res)

    print(r1.content)