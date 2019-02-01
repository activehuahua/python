from pymongo import MongoClient
from weixin.config import *
import pymongo


class MONGO():
    def __init__(self):

        try:
            self.client=MongoClient(MONGO_URL)
            self.db = self.client['weixin']
            self.collection = ''
        except  Exception as e:
            print(e.args)
    


    def save_to_mongo(self,table,result):
        self.collection=self.db[table]
        if self.collection.insert_one(result):
            print('Saved one record to Mongo!')

    def save_many_to_mongo(self,table,results):
        self.collection = self.db[table]
        if self.collection.insert_many(results):
            print('Saved many records to Mongo!')