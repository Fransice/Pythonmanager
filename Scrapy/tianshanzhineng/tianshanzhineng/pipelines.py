# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TianshanzhinengPipeline(object):
    def __init__(self):
        self.fp= open('天善智能.txt','a',encoding='utf-8')
    def process_item(self, item, spider):
        print(item["title"])
        print(item["Introduction"])
        print(item["stu"])
        print(item["link"])
        print("--------------------")
        print("")
        self.fp.write(item["title"][0]+'\n'+item["Introduction"][0]+'\n'+item["stu"][0]+'\n'+item["link"][0]+'\n\n')
        return item
    def close_spider(self):
        self.fp.close()