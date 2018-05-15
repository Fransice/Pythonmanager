# -*- coding: utf-8 -*-
import scrapy
from tianshanzhineng.items import TianshanzhinengItem
from scrapy.http import Request


class TianshanSpider(scrapy.Spider):
    name = 'tianshan'
    allowed_domains = ['hellobi.com']
    start_urls = ['https://edu.hellobi.com/course/269']

    def parse(self, response):
        item = TianshanzhinengItem()
        item["title"] = response.xpath(
            "//ol[@class='breadcrumb']/li[@class='active']/text()").extract()
        item["Introduction"] = response.xpath(
            "//div[@class='course-des']/p/text()").extract()
        item["link"] = response.xpath(
            "//ul[@class='nav nav-tabs']/li/a/@href").extract()
        item["stu"] = response.xpath(
            "//span[@class='course-view']/text()").extract()
      
        yield item
        for i in range(1, 121):
            url = 'https://edu.hellobi.com/course/' + str(i)
            yield Request(url, callback=self.parse)
