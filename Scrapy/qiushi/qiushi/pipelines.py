# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiushiPipeline(object):
    def process_item(self, item, spider):
        for item_page in range(0,len(item["content"])):
            print(item["content"][item_page])
            print(item["link"][item_page])
        return item
