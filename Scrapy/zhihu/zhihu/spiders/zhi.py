# -*- coding: utf-8 -*-
import scrapy
import json


class ZhiSpider(scrapy.Spider):
    name = 'zhi'
    allowed_domains = ['zhihu.com']
    start_urls = [
        'https://www.zhihu.com/api/v4/members/jincuodao/followers?offset=20&limit=20'
    ]

    def parse(self, response):
        print(response,encode=("utf-8"))
        List = json.loads(response.body.decode("utf-8"))["data"]
        for list_name in List["data"]:
            print(list_name["name"])
