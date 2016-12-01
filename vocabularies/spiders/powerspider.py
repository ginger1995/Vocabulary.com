# -*- coding: utf-8 -*-
import scrapy
from vocabularies.items import VocabulariesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import datetime
import socket


class PowerSpider(CrawlSpider):
    name = "powerspider"
    allowed_domains = ["www.vocabulary.com"]
    start_urls = ['https://www.vocabulary.com/dictionary/subpoena']

    rules = (
        Rule(LinkExtractor(allow=('dictionary/.')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
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
        if response.xpath('//*[@class="short"]'):
            l.nested_xpath(
                '//*[@class="short"]').add_xpath('short_exp', 'string(.)')
        if response.xpath('//*[@class="long"]'):
            l.nested_xpath(
                '//*[@class="long"]').add_xpath('long_exp', 'string(.)')
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())
        return l.load_item()
