#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     pymongo-ep1
   Description :
   Author :       zhaojianghua
   date：          2018/12/31
'''

import pymongo
from bson.objectid import  ObjectId
client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client.test  #数据库名

collection = db.students  #相当于关系型数据库的数据表

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}


student2 = {
    'id': '20170102',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1,student2])
# print(result)

# result=collection.find_one({'name':'Mike'})
# print(result)
#
# result=collection.find_one({'_id':ObjectId('5c29d391db98910fd4fcbae1')})
# print(result)

#results= collection.find({'age':{'$gt':10}})
#results= collection.find({'name':{'$regex':'^M.*'}})
# condition={'age':'Jordan'}
# student=collection.find_one(condition)
# student['age']=25

#result=collection.update(condition,student)
# condition={'age':{'$gt':19}}
# student=collection.find_one(condition)
# student['age']=25
#
# result=collection.update_one(condition,{'$set':student})


condition={'age':{'$gt':19}}
student=collection.update_many(condition,{'$inc':{'age':1}})


results=collection.find().sort('name',pymongo.DESCENDING)
print(results)
for result in results:
    print(result)