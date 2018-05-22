# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:15:55 2018

@author: xiehefang
"""

import scrapy
from scrapy.spiders import XMLFeedSpider
from sushi import items

class DouBMovieXml(XMLFeedSpider):
    name = 'DouBanMovieXml'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/review/best/']
    #namespaces = ('n','http://rdf.data-vocabulary.org/#')
    itertag = 'div'
    def parse_node(self,response,node):
        item = items.SushiXmlItem()
        item['title'] = node.xpath('//div[@class="main review-item"]/a/img/@title').extract()
        item['link'] = node.xpath('//div[@class="main review-item"]/a/@href').extract()
        return item 