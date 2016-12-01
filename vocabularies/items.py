# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class VocabulariesItem(scrapy.Item):
    # primary fields
    word = Field()
    short_exp = Field()
    long_exp = Field()

    # Housekeeping fields
    #url = Field()
    #project = Field()
    #spider = Field()
    #server = Field()
    #date = Field()
