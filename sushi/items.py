# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SushiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    voter = scrapy.Field()
    vottitle = scrapy.Field()


class SushiCrawlItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    voter = scrapy.Field()
    vottitle = scrapy.Field()
    

class SushiXmlItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    voter = scrapy.Field()
    vottitle = scrapy.Field()
    
class SushiCSVItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    voter = scrapy.Field()
    vottitle = scrapy.Field()


class SushiSitemapItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    voter = scrapy.Field()
    vottitle = scrapy.Field()