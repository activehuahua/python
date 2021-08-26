#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : pymysql-ep1.py
@Time    : 2018/12/13 14:52
@desc   :
'''
from functools import wraps
from venv import logger

import pymysql, pytest
from datetime import datetime
from Database.mysqlDb import db_conf


# 数据库配置信息

def fn_timer(fn):
    """
    计算 fn 的运算时间
    :param fn:
    :return:
    """

    @wraps(fn)  # 装饰器
    def function_timer(*args, **kwargs):
        start = datetime.now()
        result = fn(*args, **kwargs)
        print(f'{fn.__name__} total running time {datetime.now() - start} seconds')
        return result

    return function_timer


@fn_timer
def mtest_execute(connection, sql):
    rows_count = 0
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        for i in range(1000):
            rows_count += cursor.execute(sql, ('frank@python.org', 'test' + str(i)))
        connection.commit()

    return rows_count


@fn_timer
def mtest_execute_many(connection, sql):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        datas = [('webmaster@python.org', 'test' + str(i)) for i in range(1, 1000)]
        rows_count = cursor.executemany(sql, datas)
        connection.commit()

    return rows_count


if __name__ == '__main__':
    insert_sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    connection = pymysql.connect(**db_conf.TESTDB_CONFIG)
    # connection = pymysql.connect(host='localhost', port=3306, user='root',
    #                              password='Mi123456', db='sakila', charset='utf8')

    mtest_execute(connection, insert_sql)
    mtest_execute_many(connection, insert_sql)
