# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:59:48 2018

@author: xiehefang
"""

import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from sushi import items

class DouBMovieCrawl(CrawlSpider):
    name = 'DouBanMovieCrawl'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/review/best/']
    rules = (Rule(LinkExtractor(allow=('/subject/\d+',)), callback='parse2_item'),)
    
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
    
    #用Item Loaders装载Items
    def parse1_item(self,response):
        iteml = ItemLoader(item=items.SushiCrawlItem(),response=response)
        iteml.add_xpath('title','//div[@class="main review-item"]/a/img/@title')
        iteml.add_xpath('link','//div[@class="main review-item"]/a/img/@src')
        iteml.add_xpath('link','//div[@class="main review-item"]/a/@href')
        iteml.add_value('desc','hhhhhhhhhhhhh')
        return iteml.load_item()
    
    def parse2_item(self,response):
        item = items.SushiCrawlItem()
        item['voter'] = response.xpath('//div[@class="comment"]/h3/span/a[@class=""]/text()').extract()
        item['link'] = response.xpath('//div[@class="comment"]/h3/span/a[@class=""]/@href').extract()
        item['desc'] = response.xpath('//div[@class="comment"]/p/text()').extract()
        return item 