# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json

class SushiPipeline(object):
    #存成json文本
    #def process_item(self, item, spider):
        #return item
    def __init__(self):
        self.file = open('pipeline1.json','wb')
    
    def process_item(self,item,spider):       
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.encode())
        return item
    
    def close_spider(self,spider):
        self.file.close()

class DelPipeline(object):
    def process_item(self, item, spider):
        if 'https://www.douban.com/people/leave_left/' not in item['link'] :
            return item
        else:
            raise DropItem("not right url %s" % item)

'''
去重复            
class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
'''