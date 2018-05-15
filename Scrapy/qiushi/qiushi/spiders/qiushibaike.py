# -*- coding: utf-8 -*-
import scrapy
from qiushi.items import QiushiItem
from scrapy.http import Request


class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    def start_requests(self):
        ua = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
        }
        yield Request('http://qiushibaike.com/', headers=ua)

    def parse(self, response):
        item = QiushiItem()
        item["content"] = response.xpath(
            "//div[@class='content']/span/text()").extract()
        item["link"] = response.xpath(
            "//a[@class='contentHerf']/@href").extract()
        yield item
