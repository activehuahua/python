#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     pymysql-ep4
   Description :
   Author :       zhaojianghua
   date：          2018/12/31
'''
from Database.mysqlDb import  db_conf
import pymysql

if __name__ == '__main__':
    table = 'issuess'
    sql = f'select * from {table} where issue>5 '

    try:
        connect = pymysql.connect(**db_conf.TESTDB_CONFIG)
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        aa=cursor.execute(sql)  # 此处的插入数据需要转化成list，转成 tuple元组也可以
        count=cursor.rowcount

        # row=cursor.fetchone()

        # while row:
        #     print(row)
        #     row=cursor.fetchone()

        rows=cursor.fetchmany(aa)
        for item in rows:
            print(item)
    finally:
        connect.close()

    # print(  values )
    # print(sql)