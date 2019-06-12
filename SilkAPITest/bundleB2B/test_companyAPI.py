# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 11:27
# @Author  : zhaojianghua
# @File    : companyAPI.py
# @Software: PyCharm
# @Desc    : 测试ERP Company数据导入接口
import json

import requests
import base64
from time import sleep
import pytest

#DEv
# URL='https://fl4mq0bm40.execute-api.us-west-2.amazonaws.com/prod'
# Store_hash='h3jnjw30qw'

#Staging
URL='https://dk0xoldgn8.execute-api.us-west-2.amazonaws.com/prod'
Store_hash='wao5z0rn37'


Filename='company.json'
CompanyName='Company Alex 8'
CompanyNames='Company Alex 8,Ferrell Zhang'

def getBase64Content():

    data = base64.b64encode(open(Filename, "rb").read())
    content=data.decode(encoding='utf-8')
    print(content)
    return content

param={
    "store_hash":Store_hash,
    "data":getBase64Content(),
    "file_name":Filename
}


def test_importCompany():
    '''导入json文件'''
    #global URL
    s=requests.Session()
    print(param)
    r=requests.post(URL+'/companyLead',data=json.dumps(param))
    print(r.url)

    id=parseId(r.text)
    sleep(10)
    status = checkResult(id)
    assert status == '1'

def parseId(content):
    '''解析对应的id值'''
    content=content.replace('\\n','').replace('\\', '')
    jsonStr=json.loads(content)
   # print(jsonStr)
    id=jsonStr["id"]
    print(id)
    return id

def parseStatus(result):
    '''解析对应的status值'''
    result = result.replace('\\n', '').replace('\\', '')
    jsonStr = json.loads(result)
    # print(jsonStr)
    status = jsonStr["status"]
    print(status)
    return status

def checkResult(id):
    '''检查导入结果是不是正确'''
    param={
        "store_hash": Store_hash,
        "id":id
    }
    r=requests.get(URL+'/checkData', params=param)
    print(r.url)
    print(r.content)
    status=parseStatus(r.text)
    return status

def test_export_single_Company():
    '''单公司导出'''
    param = {
        "store_hash": Store_hash,
        "companyNames": CompanyName
    }
    r = requests.get(URL + '/companyLead', params=param)
    #print(r.content)
    id=parseId(r.text)
    #print('id=',id)
    sleep(15)
    status=checkResult(id)
    assert status=='1'


def test_export_many_Company():
    '''多公司导出'''
    param = {
        "store_hash": Store_hash,
        "companyNames": CompanyNames
    }
    r = requests.get(URL + '/companyLead', params=param)
    print(r.content)
    id=parseId(r.text)
    print('id=',id)
    sleep(5)
    status = checkResult(id)
    assert status == '1'

def test_export_all_Companys():
    '''多公司导出'''
    param = {
        "store_hash": Store_hash,
        "companyNames": ''
    }
    r = requests.get(URL + '/companyLead', params=param)
    print(r.content)
    id=parseId(r.text)
    print('id=',id)
    sleep(15)
    status = checkResult(id)
    assert status == '1'


def test_checkData():
    id=373936313376838121
    param={
        "store_hash": Store_hash,
        "id":id
    }
    r=requests.get(URL+'/checkData', params=param)
    print(r.url)
    print(r.content)
    status=parseStatus(r.text)
    assert status == '1'


if __name__ == '__main__':
    test_importCompany()