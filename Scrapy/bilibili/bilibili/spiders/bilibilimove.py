# -*- coding: utf-8 -*-
import scrapy
import json


class BilibilimoveSpider(scrapy.Spider):
    name = 'bilibilimove'
    allowed_domains = ['bilibili.com']

    def start_requests(self):
        #https://api.bilibili.com/x/web-interface/newlist?callback=jQuery172008293058940662035_1523242239790&rid=24&type=0&pn=1&ps=20&jsonp=jsonp&_=1523242240185
        for page_num in range(0, 999999):
            url = 'https://api.bilibili.com/x/web-interface/newlist?&rid=24&type=0&pn=' + str(
                page_num) + '&ps=20&jsonp=jsonp&_=1523242240185'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        for target_list in json.loads(response.body.decode('utf-8'))["data"]["archives"]:
            yield target_list