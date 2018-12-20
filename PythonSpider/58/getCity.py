#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : getCity.py
@Time    : 2018/12/20 10:37
@desc   :
'''

from bs4 import BeautifulSoup
import requests, re
import json
import time
from requests.exceptions import RequestException
import os, string
from lxml import etree
import pymysql
from db_conf import *
import os.path

# 蘑菇代理的隧道订单
appKey = "cE9KZWZoOGJaV0NEWlAzRzpUYnpsNkNzaTl4TloxdkEw"

# 蘑菇隧道代理服务器地址
ip_port = 'transfer.mogumiao.com:9001'

url = 'https://www.58.com/changecity.html'
proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
   # "Proxy-Authorization": 'Basic '+ appKey
    }
requests.packages.urllib3.disable_warnings()

def get_html(pageUrl):

    try:
       # req = requests.get(pageUrl, headers=headers, proxies=proxy,verify=False,allow_redirects=False)
        req = requests.get(pageUrl, headers=headers)

        # print(req.text)
        if (req.status_code == 200):
            html = req.text
            return html
        # if (req.status_code== 302 or req.status_code==301):
        #     loc=req.headers['Location']
        #     url_f=pageUrl+loc
        #     req=requests.get(url_f, headers=headers, proxies=proxy,verify=False,allow_redirects=False)
        #     html = req.text
        #     return html
        return None
    except RequestException as e:
        return None


def get_cityUrl_cityName(html):
    try:
        pattern = re.compile('var cityList = {(.*?)</script>', re.S)
        result = re.findall(pattern, html)
        result = str(result)
        result = result.replace(r'\n', '').replace('\r', '').replace(' ', '').replace('"', '')
        patter2 = re.compile('.*?:{(.*?)},', re.S)
        citys = re.findall(patter2, result)
        allCitys = []
        for item in citys:
            cityList = item.split(',')
            for city in cityList:
                allCitys.append(city)
        cityDict = {}
        for item in allCitys:
            key = item.split(':')[0]
            value = item.split(':')[1].split('|')[0]
            value = 'https://' + value + '.58.com/ershoufang/'
            cityDict[key] = value
        write_dict_toFile(cityDict)
        return cityDict
    except Exception  :
        #raise Exception
        return None
    finally:
        return cityDict

def write_dict_toFile(list):
    file='dict.txt'
    result=str(list)
    result=result.replace('[','').replace(']','').replace('\'','')
    with open(file,'a+') as f:
        f.write(result+'\n')

def get_canton(pageUrl):
    #pageUrl = 'https://hexian.58.com/ershoufang/'
    time.sleep(5)
    html = get_html(pageUrl)
    html = etree.HTML(html)
    result = html.xpath('//div[@class="filter-wrap"]/dl[1]//dd[1]/a/text()')
    cantonList = []
    if result==None or len(result)==0:
        result=html.xpath('//div[@class="filter-wrap"]//div[@id="qySelectFirst"]/a[position()>0]/text()')
    has_qita=False
    for item in range(1, len(result)):
        result[item] = result[item].replace('\n', '').replace(' ', '').strip()
        if result[item].strip()=='其他':
            has_qita=True
        cantonList.append(result[item])
    if has_qita==False:
        cantonList.append('其他')
  # print(cantonList)
    return cantonList

def get_cityCode(cityName='北京', connection=None):
    sql = f'select cityCode from city where cityName="{cityName}"'
    result = ' '
    try:
        mycusor = connection.cursor()
        mycusor.execute(sql)
        result: object = mycusor.fetchone()[0].strip()
        if result == None:
            result=' '
   # print(result)
        return result
    except Exception as e:
        print(e.reason)
    finally:
        return result

def  deal_data(name,cityCode,pageUrl,cantonsList):
    lists=[]
    cantons=''
    lists.append(name)
    lists.append(cityCode)
    lists.append(pageUrl)
    for item in cantonList:
        cantons=cantons+item+' '
    cantons=cantons.rstrip()
    lists.append(cantons)
    write_cityInfo_toFile(lists)
   # print(lists)
    #return lists

def write_cityInfo_toFile(list):
    file='cities_'+time.strftime('%Y%m%d')+'.txt'
    result=str(list)
    result=result.replace('[','').replace(']','').replace('\'','')
    with open(file,'a+') as f:
        f.write(result+'\n')


if __name__ == '__main__':
    html = get_html(url)
    # print(html)
    try:
        connection = pymysql.connect(**TESTDB_CONFIG)
        cityDicts= get_cityUrl_cityName(html)
        print(cityDicts)
        for key,value in cityDicts.items():
            cantonDataList=[]
            pageUrl=cityDicts[key].strip()
            cityCode=get_cityCode(key, connection)
            cantonList=get_canton(pageUrl)
            deal_data(key,cityCode,pageUrl,cantonList)
    except Exception as e:
        raise Exception

    finally:
        connection.close()
