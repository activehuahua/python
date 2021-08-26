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
    host='localhost',
    user='root',
    passwd='Mi123456',
    database='sakila'
)

TESTDB_CONFIG = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'Mi123456',
    'db':'sakila',
   'charset': 'utf8'
}