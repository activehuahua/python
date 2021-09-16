
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


if __name__ == '__main__':
    url='https://stock.tuchong.com/topic?topicId=50064'
    topicId=common.getTopicId(url)
    print(topicId)
