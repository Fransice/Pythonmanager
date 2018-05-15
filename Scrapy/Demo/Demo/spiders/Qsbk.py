# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Demo.items import DemoItem
from scrapy.http import Request


class QsbkSpider(CrawlSpider):
    name = 'Qsbk'
    allowed_domains = ['qiushibaike.com']

    def start_requests(self):
        ua = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
        }
        yield Request('http://qiushibaike.com/', headers=ua)

    rules = (Rule(
        LinkExtractor(allow=r'article'), callback='parse_item', follow=True), )

    def parse_item(self, response):
        i = DemoItem()
        i["content"] = response.xpath(
            "//div[@class='content']/text()").extract()
        i["link"] = response.xpath("//link[@rel='canonical']/@href").extract()
        print(i["content"])
        print(i["link"])
        return i
