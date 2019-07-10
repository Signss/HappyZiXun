# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
"""
target_website: http://www.cecet.cn/
spider_type: general
author: strict

"""

class HappynewsSpider(CrawlSpider):
    name = 'happynews'
    allowed_domains = ['www.cecet.cn/']
    start_urls = ['http://www.cecet.cn/ent/0001/list_26_1.shtml']

    rules = (
        # 匹配新闻列表页url
        Rule(LinkExtractor(restrict_xpaths='/html/body/center/div[3]/div[1]/div/div/div/a[11]'), follow=True),
        # 匹配新闻详情页url
        Rule(LinkExtractor(allow=r'http://www.cecet.cn/ent/(\d)*/(\d)*.shtml', restrict_xpaths='//*[@class="newslist"]/dl'),callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        pass


