#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : heroskins.py
@Time    : 2018/12/27 9:34
@desc   :

https://ossweb-img.qq.com/images/lol/web201310/skin/big     266     000    .jpg
'''
import requests,re,json
#
base_url="https://ossweb-img.qq.com/images/lol/web201310/skin/big"
hero_url="https://lol.qq.com/biz/hero/champion.js"

hero_result=requests.get(hero_url).text


hero_dict=re.search('{"keys":(.*?),"data":',hero_result).group(1)
hero_dict=json.loads(hero_dict)
#print(hero_dict)

for key,value in hero_dict.items():
    print(key,value)
    for num in range(15):
        skin_img_url=base_url + str(key)+'%03d' %(num)+'.jpg'
        print(skin_img_url)
        if requests.get(skin_img_url).status_code == 200:
            img_file= 'img/'+str(value)+'%d' %(num)+'.jpg'
            with open(img_file,'wb') as f :
                f.write(requests.get(skin_img_url).content)