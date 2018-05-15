# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class BilibiliPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[dbname]
        self.post=tdb[settings["MONGODB_DOCNAME"]]
    def process_item(self, item, spider):
        move = dict(item)
        self.post.insert(move)
        return item
