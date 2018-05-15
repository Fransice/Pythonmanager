# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept':
    'application/json, text/plain, */*',
    'accept-encoding':
    'gzip, deflate, br',
    'accept-language':
    'zh-CN,zh;q=0.9',
    'authorization':
    'Bearer 2|1:0|10:1521685171|4:z_c0|92:Mi4xWnRXLUFnQUFBQUFBa0lMa1dqcTdEQ1lBQUFCZ0FsVk5zMkNnV3dCbmM3X2Vwai1YZGdLREMyU3p6Y2p4RXhmT25n|ee6743312ef9b5d872099e99d571caa9cff0f10254bf243e5e409f22ee2775fb',
    'cookie':
    'd_c0="AJCC5Fo6uwyPTiyw9fdnjd75tVBXi8PxbS4=|1511503085"; _zap=99858dfe-1a99-4302-9165-1982b1407b4f; l_cap_id="NjgwYjgxOTM5N2EwNGU4MWJmZjg4MzI3YTRjMTRhNDg=|1521616708|6d1f364d1f151add00c02f150e4a5ed492610428"; r_cap_id="MzdhZGVjZGQzYTQxNDhhYWFjYTliZjJmNzA2ZGI5NWE=|1521616708|30e904532d623eeeaa993a75ca187a7f06589498"; cap_id="OTc5OTJhOTVjOWFmNGIwZDg3OTY0YTA4YTc2MTRmMDM=|1521616708|e4bc009d70b725732e4407ab190a12ef5e761cd0"; capsion_ticket="2|1:0|10:1521685164|14:capsion_ticket|44:ODBjN2UwODQ4YTY3NDZiZjlmOWQyMDlmNDUxOTJmMDI=|4b7915cb982fd69d8a67a4c8a089df896f16638c67472a5e46841b2a0fb8cea2"; z_c0="2|1:0|10:1521685171|4:z_c0|92:Mi4xWnRXLUFnQUFBQUFBa0lMa1dqcTdEQ1lBQUFCZ0FsVk5zMkNnV3dCbmM3X2Vwai1YZGdLREMyU3p6Y2p4RXhmT25n|ee6743312ef9b5d872099e99d571caa9cff0f10254bf243e5e409f22ee2775fb"; q_c1=101e983fb1bf4fe78eca42a3f249522f|1522290713000|1511503084000; __DAYU_PP=jvZMvbYqaVEE7BYErEQfffffffffec96e147d146; _xsrf=f35f5609-f2de-4134-8b5b-392d98c9f3bc; __utma=51854390.812074301.1522655132.1522655132.1523250872.2; __utmc=51854390; __utmz=51854390.1523250872.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/zhang-19-9/collections; __utmv=51854390.100-1|2=registration_date=20160312=1^3=entry_date=20160312=1',
    'referer':
    'https://www.zhihu.com/people/jincuodao/activities',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu.pipelines.ZhihuPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
