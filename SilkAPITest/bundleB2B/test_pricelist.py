# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 11:01
# @Author  : zhaojianghua
# @File    : test_pricelist.py
# @Software: PyCharm
# @Desc    :
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


Filename='originvariants.json'
CompanyName='Company Alex 8'
CompanyNames='Company Alex 8,Alex Staging Company'

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


def test_importPriceList():
    '''导入json文件'''
    s=requests.Session()
    print(param)
    r=s.post(URL+'/catalogProductLead',data=json.dumps(param))
    print(r.text)
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

# def test_export_single_Company():
#     '''单公司导出'''
#     param = {
#         "store_hash": Store_hash,
#         "companyNames": CompanyName
#     }
#     r = requests.get(URL + '/companyLead', params=param)
#     #print(r.content)
#     id=parseId(r.text)
#     #print('id=',id)
#     sleep(15)
#     status=checkResult(id)
#     assert status=='1'
#
#
# def test_export_many_Company():
#     '''多公司导出'''
#     param = {
#         "store_hash": Store_hash,
#         "companyNames": CompanyNames
#     }
#     r = requests.get(URL + '/companyLead', params=param)
#     print(r.content)
#     id=parseId(r.text)
#     print('id=',id)
#     sleep(5)
#     status = checkResult(id)
#     assert status == '1'
#
# def test_export_all_Companys():
#     '''多公司导出'''
#     param = {
#         "store_hash": Store_hash,
#         "companyNames": ''
#     }
#     r = requests.get(URL + '/companyLead', params=param)
#     print(r.content)
#     id=parseId(r.text)
#     print('id=',id)
#     sleep(15)
#     status = checkResult(id)
#     assert status == '1'
#

def test_checkData():
    id=13462184510309732841
    param={
        "store_hash": Store_hash,
        "id":id
    }
    r=requests.get(URL+'/checkData', params=param)
    print(r.url)
    print(r.content)
    status=parseStatus(r.text)
    assert status == '1'