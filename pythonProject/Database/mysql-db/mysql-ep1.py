#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : mysql-ep1.py
@Time    : 2018/12/13 14:08
@desc   :
'''

import db_conf

mycusor=db_conf.mydb_test.cursor()
sql="insert into issuess(`issue`,`release`,`author`) values (%s,%s,%s)"
val=[
    (12,'11.0.0','alex1'),
    (13,'11.0.1','alex2')
]
mycusor.executemany(sql,val)
db_conf.mydb_test.commit()
print(mycusor.rowcount,'记录插入成功')

sql='select * from issuess'
mycusor.execute(sql)
result=mycusor.fetchall()
print(result)
for item in range(len(result)):
    print(result[item])

mycusor.close()