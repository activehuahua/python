#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : db_conf.py
@Time    : 2018/12/13 14:21
@desc   :
'''

import mysql.connector
import pymysql
mydb_test= mysql.connector.Connect(
    host='172.28.1.247',
    user='root',
    passwd='kzO2Rgel6xs80a3JYKB2',
    database='test'
)

TESTDB_CONFIG = {
    'host':'172.28.1.247',
    'port':3306,
    'user':'root',
    'password':'kzO2Rgel6xs80a3JYKB2',
    'db':'test',
   'charset': 'utf8'
}