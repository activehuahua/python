
# -*- coding: utf-8 -*-#

'''
# Name:         common
# Description:  
# Author:       alex
# Date:         2021/9/16
'''
import re,json

class common:
    def getTopicId(url):
        partten=re.compile('.*?topicId=(\d+)',re.S)
        result=re.match(partten,url)
        topicId=result.group(1)
        return topicId

    def getResult():
        goods = r"goods=[{'name':'alex','age':false},{'name':'bob','age':False}];"
        result = [{'name': 'alex', 'age': '20'}, {'name': 'bob', 'age': '30'}]

        print(goods)
        pattern = re.compile(r"goods=\[(.*)\];", re.S)
        result = pattern.findall(goods)
        str=result[0]
        str=str.replace('false','False')

        result=list(eval(result[0].replace('false','False')))
        print(result.__len__())

    def getResult1():
        goods = r"goods=[{'name':'alex','age':'20'},{'name':'bob','age':'30'}]"
        result = [{'name': 'alex', 'age': '20'}, {'name': 'bob', 'age': '30'}]

        print(goods)
        pattern = re.compile(r"'name':(.*?),", re.S)
        result = pattern.findall(goods)

if __name__ == '__main__':
    url='https://stock.tuchong.com/topic?topicId=50064'
    topicId=common.getTopicId(url)
    # print(topicId)
    common.getResult()