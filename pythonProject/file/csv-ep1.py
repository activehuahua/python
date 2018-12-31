#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     csv-ep1
   Description :
   Author :       zhaojianghua
   date：          2018/12/29
'''

import  csv

# with open('data.csv','w') as csvfile:
#     writer= csv.writer(csvfile)
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','Mike','20'])
#     writer.writerow(['10002', 'Bob', '22'])
#     writer.writerow(['10003', 'Jordan', '21'])

with open('data.csv','w') as csvfile:
    fieldnames=['id','name','age']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001','name':'Mike','age':20})
    writer.writerow({'id':'10002','name':'Bob','age':22})
    writer.writerow({'id':'10003','name':'Jordan','age':21})