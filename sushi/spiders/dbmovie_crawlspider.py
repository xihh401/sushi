# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:59:48 2018

@author: xiehefang
"""

import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from sushi import items

class DouBMovieCrawl(CrawlSpider):
    name = 'DouBanMovieCrawl'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/']
    
    rules = (Rule(LinkExtractor(allow=('https\:\/\/movie\.douban\.com', )), callback='parse_item'),)
    
    def parse_item(self,response):
        #self.log('%s' % response.url)
        item = items.SushiCrawlItem()
        #for sel in response.xpath('//div[@typeof="v:Review"]'):
        #for sel in response.xpath('//div[@class="review-list chart "]'):
        item['title'] = response.xpath('//div[@class="main review-item"]/a/img/@title').extract()
        item['link'] = response.xpath('//div[@class="main review-item"]/a/@href').extract()
        #yield item
        #print(item)
        return item
