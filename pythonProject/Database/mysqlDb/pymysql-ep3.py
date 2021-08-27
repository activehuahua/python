#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     pymysql-ep2
   Description :
   Author :       zhaojianghua
   date：          2018/12/30

   数据不存在则插入，存在则更新
'''

import pymysql
from Database.mysqlDb import db_conf


data = {
    '`issue`': '5',
    '`release`': '12.0.1',
    '`author`': 'zhaojianghua',
    '`note`': '654321发的规范的'
}


if __name__ == '__main__':
    table = 'issuess'

    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))  # %s 占位符
    # values=list(data.values())

    sql = f'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '
    update = ','.join(["{key}=%s".format(key=key) for key in data])

    sql = sql + update
    print(sql)

    try:
        connect = pymysql.connect(**db_conf.TESTDB_CONFIG)
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, tuple(data.values())*2)  # 此处的插入数据需要转化成list，转成 tuple元组也可以
        connect.commit()
    except Exception as e:

        connect.rollback()
        print(e)
    finally:
        connect.close()

