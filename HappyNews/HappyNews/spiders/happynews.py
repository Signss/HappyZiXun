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
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
