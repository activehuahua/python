# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 11:16
# @Author  : zhaojianghua
# @File    : getPrice.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
import requests
import pyquery
from lxml import etree
from pyquery import PyQuery as pq

class ccfdcClass():
    def __init__(self):
        self.baseurl='http://www.ccfdw.gov.cn/ecdomain/lpcs/xmxx/huxx.jsp'
        self.result=[]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
        }

    def getSubUrl(self):
        with open('houselists.txt','r') as f:
            singleHouse=f.readlines()

            self.result.append(singleHouse)


    def getPrice(self,houseId,loudongId):
        loudongId=str(loudongId).replace('\n','')
        url=self.baseurl + '?hid=' + houseId + '&lid=' +loudongId
        url=url.replace('\n','')
        print(url)
        r=requests.get(url,headers=self.headers)
        doc=pq(r.text)
        td_houseName = doc('td').eq(4).text()
        td_unitPrice = doc('td').eq(28).text()
        list=[]
        list.append(td_houseName)
        list.append(td_unitPrice)
        list.append(houseId)
        list.append(loudongId)
        priceResult=','.join(list)
        print(priceResult)
        self.writeResult(priceResult,'priceResult.txt')

    def getUrls(self):
        with open('houselists.txt', 'r') as f:
            singleHouse = f.readlines()
            self.result.append(singleHouse)

        list1=self.result[0]

        for item in list1:
            list=item.split(',')
            self.getPrice(list[0],list[1])

    def writeResult(self,pricelist,filename):
        with open(filename,'a+') as f:
            f.writelines(pricelist+"\n")

    def getSQL(self):
        file=open('priceResult.txt','r')
        try:
            while True:
                text_line=file.readline()
                if text_line:
                    list=text_line.split(',')
                    name=list[0]
                    price=list[1].replace('元/平方米','')
                    houseId=list[2]
                    strSQL=f'update t_project_room set  presale_price={price} where spider_room_id="{houseId}" and name={name};'
                    self.writeResult(strSQL, 'price_SQL.sql')
                else:
                    break
        finally:
            file.close()




if __name__ == '__main__':
    myprice=ccfdcClass()
    #myprice.getUrls()
    myprice.getSQL()