#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     pymysql-ep2
   Description :
   Author :       zhaojianghua
   date：          2018/12/30

   数据表增加了字段，插入的sql语句不需要更改，只需要修改插入的数据，增加新增字段即可
'''

import pymysql
import db_conf

data={
    '`issue`':'14',
    '`release`':'12.0.1',
    '`author`':'zhaojianghua',
    'note':'123456'
}

table='issuess'

keys=','.join(data.keys())
values=','.join(['%s']*len(data))  # %s 占位符
#values=list(data.values())

sql=f'INSERT INTO {table}({keys}) VALUES ({values})'

if __name__ == '__main__':
    try:
        connect=pymysql.connect(**db_conf.TESTDB_CONFIG)
        cursor=connect.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql,tuple(data.values()))  # 此处的插入数据需要转化成list，转成 tuple元组也可以
        connect.commit()
    except Exception as e :

        connect.rollback()
        print(e)
    finally:
        connect.close()

    # print(  values )
    # print(sql)