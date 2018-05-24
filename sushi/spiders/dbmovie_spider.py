# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:35:35 2018

@author: xiehefang
"""

import scrapy
from sushi import items

class DouBMovieSpider(scrapy.Spider):
    name = 'DouBanMovie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/review/best/']
    '''
    example
    
    def start_requests(self):
        return [scrapy.FormRequest("http://www.example.com/login",
                               formdata={'user': 'john', 'pass': 'secret'},
                               callback=self.logged_in)]

    def logged_in(self, response):
    # here you would extract links to follow and return Requests for
    # each of them, with another callback
        pass
    '''
    
    def parse(self,response):
        #filename = 'doubanmovie'
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        response.selector.remove_namespaces()
        Item = items.SushiItem()
        for sel in response.xpath('//div[@typeof="v:Review"]'):
            yield Item
            #xpath支持正则表达式匹配，re.test()
            #Item['title'] = sel.xpath('//div[re:test(@class, "main review-\s$")]/a/img/@title').extract()
            Item['title'] = sel.xpath('//div[@class="main review-item"]/a/img/@title').extract()
            Item['link'] = sel.xpath('//div[@class="main review-item"]/a/@href').extract()
            Item['voter'] = sel.xpath('//a[@class="name"]/text()').extract()
            Item['vottitle'] = sel.xpath('//div[@class="main-bd"]/h2/a/text()').extract()
            
        #print(Item)
            