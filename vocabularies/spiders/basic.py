# -*- coding: utf-8 -*-
import scrapy
from vocabularies.items import VocabulariesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
import datetime
import socket

class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["www.vocabulary.com"]
    start_urls = ['http://www.vocabulary.com/dictionary/felony','http://www.vocabulary.com/dictionary/arson']

    def parse(self, response):

        '''This function parses a property page.
		@url http://www.vocabulary.com/dictionary/felony
		@returns items 1
		@scrapes word short_exp long_exp
		@scrapes url project spider server date
        '''

        '''
        self.log("THE WORD: %s" % response.xpath(
            '//*[@class="dynamictext"]/text()').extract()[0])
        self.log("THE BRIEF EXPLAINING: %s" % response.xpath(
            '//*[@class="short"]')[0].xpath('string(.)').extract()[0])
        self.log("THE EXPLICT EXPLAINING: %s" % response.xpath(
            '//*[@class="long"]')[0].xpath('string(.)').extract()[0])
        '''
        '''
        item = VocabulariesItem()
        item['word'] = response.xpath(
            '//*[@class="dynamictext"]/text()').extract()[0]
        item['short_exp'] = response.xpath(
            '//*[@class="short"]')[0].xpath('string(.)').extract()[0]
        item['long_exp'] = response.xpath(
            '//*[@class="long"]')[0].xpath('string(.)').extract()[0]
        '''

        # Create the loader using the response
        l = ItemLoader(item=VocabulariesItem(), response=response)
        # Load fields using Xpath expressions
        l.add_xpath('word', '//*[@class="dynamictext"]/text()')
        l.nested_xpath(
            '//*[@class="short"]').add_xpath('short_exp', 'string(.)')
        l.nested_xpath('//*[@class="long"]').add_xpath('long_exp', 'string(.)')
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())
        return l.load_item()
