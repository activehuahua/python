#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : mysql-ep1.py
@Time    : 2018/12/13 14:08
@desc   :
'''

from Database.mysqlDb import db_conf

mycusor=db_conf.mydb_test.cursor()
sql="insert into issuess(`release`,`author`) values (%s,%s)"
val=[
    ('11.0.2','alex1'),
    ('11.0.3','alex2')
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