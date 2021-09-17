# -*- coding: utf-8 -*-#

'''
# Name:         getImageByAlbumID
# Description:  
# Author:       alex
# Date:         2021/9/16
#               https://stock.tuchong.com/topic?topicId=50064
'''
from common import *
import requests, re, json, faker
from faker import Faker


class getImageByAlbumID():
    def setHeader(self):
        ua = Faker()
        self.header = {}
        self.header['user-agent'] = ua.user_agent()

    def getHtml(self, url):
        self.setHeader()
        req = requests.get(url, headers=self.header)
        content = req.text
        # print(content)
        return content

    def getImageID(self,content):

        pattern = re.compile('goods=\[(.*)\];\n</script>', re.S)
        result=re.findall(pattern,content)
        result=list(eval(result[0].replace('false','False').replace('true','True')))


        print(type(result))
        for i in range(len(result)):
            print(result[i])

    def downloadImages(self):
        pass

    def logImages(self):
        pass

    def writeToTextFile(self,content):
        with open('content.txt','a', encoding='UTF-8') as f:
            f.write(content)


if __name__ == '__main__':
    url = 'https://stock.tuchong.com/topic?topicId=50064'
    topicId = common.getTopicId(url)

    print(topicId)

    album = getImageByAlbumID()
    content=album.getHtml(url)
    album.writeToTextFile(content)
    album.getImageID(content)
