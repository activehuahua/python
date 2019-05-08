#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : demo.py
@Time    : 2019/5/7 14:34
@desc   :
'''

import boto3
db3 = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', aws_secret_access_key='ticTacToeSampleApp', aws_access_key_id='ticTacToeSampleApp', region_name='us-west-2')

db3.meta.client.list_tables()
