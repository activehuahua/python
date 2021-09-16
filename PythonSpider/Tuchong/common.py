
# -*- coding: utf-8 -*-#

'''
# Name:         common
# Description:  
# Author:       alex
# Date:         2021/9/16
'''
import re

class common:
    def getTopicId(url):
        partten=re.compile('.*?topicId=(\d+)',re.S)
        result=re.match(partten,url)
        topicId=result.group(1)
        return topicId


    def getResult():
        goods=r"goods=[{'name':'alex','age':'20'},{'name':'bob','age':'30'}];"
        result=[{'name':'alex','age':'20'},{'name':'bob','age':'30'}]
        print(result)
        print(len(result))
        print(type(result))
        for i in range(len(result)):
            print(result[i])

        goods=goods.replace(';','')
        print(goods)
        pattern = re.compile('goods=(.*)', re.S)
        # result=re.findall(pattern,goods)
        result=pattern.findall(goods)


        result=list(result)

        print(len(result))
        print(type(result))
        for i in range(len(result)):
            print(result[i])


if __name__ == '__main__':
    url='https://stock.tuchong.com/topic?topicId=50064'
    topicId=common.getTopicId(url)
    common.getResult()


