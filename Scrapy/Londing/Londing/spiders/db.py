# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }

    # start_urls = ['http://douban.com/']
    def start_requests(self):
        return [
            Request(
                "https://accounts.douban.com/login",
                callback=self.parse,
                meta={"cookiejar": 1})
        ]

    def parse(self, response):
        url = 'https://accounts.douban.com/login'
        print("没有验证码")
        data = {
            "form_email": "17703768649",
            "form_password": "a112233445566a",
            "redir": "https://www.douban.com/people/131811379/"
        }
        print("登录中...")
        return [
            FormRequest.from_response(
                response,
                meta={"cookiejar": response.meta["cookiejar"]},
                headers=self.headers,
                format=data,
                callback=self.next)
        ]

    def next(self, response):
        print("登录成功")
        title = response.xpath("/html/head/title/text()").extract()
        print(title)