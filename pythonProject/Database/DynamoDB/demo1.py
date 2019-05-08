#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : demo1.py
@Time    : 2019/5/7 14:23
@desc   :
'''

# -*- coding:utf-8 -*-

import boto3
from boto3.dynamodb.conditions import Key, Attr

# dynamodb = boto3.resource('dynamodb', region_name='us-west-2',
#                           endpoint_url='http://localhost:8000')

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', aws_secret_access_key='ticTacToeSampleApp', aws_access_key_id='ticTacToeSampleApp', region_name='us-west-2')

def table_create():
    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='users')

def table_get():
    return dynamodb.Table('users')

def item_put():
    table = table_get()
    table.put_item(
        Item={
                'username': 'liujinliu',
                'first_name': 'Jinliu',
                'last_name': 'liu',
                'age': 30,
                'account_type': 'standard_user',
            }
    )

def item_get():
    table = table_get()
    response = table.get_item(
        Key={
            'username': 'liujinliu',
            'last_name': 'liu',
        }
    )
    item = response['Item']
    return item

def item_update():
    table = table_get()
    table.update_item(
        Key={
            'username': 'liujinliu',
            'last_name': 'liu'
        },
        UpdateExpression='SET age = :val1',
        ExpressionAttributeValues={
            ':val1': 26
        }
    )

def item_delete():
    table = table_get()
    table.delete_item(
        Key={
            'username': 'liujinliu',
            'last_name': 'liu'
        }
    )

def table_size():
    table = table_get()
    return table.item_count

items = [
    {
        'username': 'liujinliu',
        'last_name': 'liu',
        'first_name': 'jinliu',
        'age': 25,
        'address': {
            'road': '1 Jefferson Street',
            'city': 'LA',
            'state': 'CA',
            'zipcode': '90001'
        }
    },
    {
        'username': 'wangyiyang',
        'last_name': 'wang',
        'first_name': 'yiyang',
        'age': 26,
        'address': {
            'road': 'huilongguan',
            'city': 'Beijing',
            'state': 'CHINA',
            'zipcode': '082'
        }
    },
    {
        'username': 'chenwenquan',
        'last_name': 'chen',
        'first_name': 'wenquan',
        'age': 27,
        'address': {
            'road': 'jintailu',
            'city': 'henan',
            'state': 'JP',
            'zipcode': '222'
        }
    },
    {
        'username': 'dengliangju',
        'last_name': 'deng',
        'first_name': 'liangju',
        'age': 28,
        'address': {
            'road': 'qingnianlu',
            'city': 'chengdu',
            'state': 'India',
            'zipcode': '333'
        }
    },
]


def batch_write():
    table = table_get()
    with table.batch_writer(overwrite_by_pkeys=['username',
                                                'last_name']) as batch:
        for item in items:
            batch.put_item(Item=item)

def query():
    table = table_get()
    response = table.query(
        KeyConditionExpression=Key('username').eq('wangyiyang')
    )
    items = response['Items']
    return items


def scan():
    table = table_get()
    response = table.scan(
        FilterExpression=Attr('age').gt(0)
    )
    items = response['Items']
    return items


def scan_1():
    table = table_get()
    response = table.scan(
        FilterExpression=Attr('age').lt(28) & Attr(
            'address.city').begins_with('B')
    )
    items = response.get('Items', [])
    return items

def table_delete():
    table = table_get()
    table.delete()

if __name__ == '__main__':
    #table_create()
    # item_put()
    print(item_get())
    # item_update()
    # print(item_get())
    # print(table_size())
    # item_delete()
    print(table_size())
    #batch_write()
    #print(table_size())
    # print(item_get())
    print(query())
    print(scan())
    #print(scan_1())
    # table_delete()
    # print(query())