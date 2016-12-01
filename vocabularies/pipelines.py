# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

'''
This pipeline aims to:
	1.drop duplicate items 
	2.drop items whose short_exp and long_exp fields are null
	3.save reliable word items to mySQL database
'''
class VocabulariesPipeline(object):
    def process_item(self, item, spider):
        return item
