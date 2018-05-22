# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:58:46 2018

@author: xiehefang
"""

import scrapy
from scrapy.spiders import SitemapSpider
from sushi import items
#import gzip

class DouBMovieSitemap(SitemapSpider):
    name = 'DouBanMovieSitemap'
    #sitemap_urls = ['https://www.douban.com/robots.txt']
    #sitemap.xml.gz暂时不会在线解压，故换一个网站抓取
    sitemap_urls = ['https://bbs.hupu.com/robots.txt']
    sitemap_rules = [
        ('/16354798.html', 'parse_xml'), 
        ('/16363357.html', 'parse1_xml'), 
        ]
    sitemap_follow = ['/sitemaps_hupu_20160528.xml']
    
    def parse_xml(self,response):
        item = items.SushiSitemapItem()
        item['voter'] = response.xpath('//div[@class="j_u"]/a/img/@alt').extract()
        return item
    
    def parse1_xml(self,response):
        item = items.SushiSitemapItem()
        item['voter'] = response.xpath('//div[@class="j_u"]/a/img/@alt').extract()
        return item
        
    
    