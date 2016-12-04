# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import pymysql
'''
This pipeline aims to:
	1st.drop items whose short_exp and long_exp fields are null
	2nd.drop duplicate items
	3rd.save reliable word items to mySQL database
'''


class VocabulariesPipeline(object):

    def __init__(self):
        # prepare work 1: build the mysql database connection.
        self.conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
                                    user='root', passwd='root', db='mysql', charset='utf8')
        self.cur = self.conn.cursor()
        self.cur.execute("USE lexicon")
        # prepare work 2: declare a new empty set to verify duplicate.
        self.word_exist = set()

    def save_to_mysql(self, item):
        self.cur.execute(
            "INSERT INTO wordbank (word, short_exp, long_exp) VALUES (\"%s\",\"%s\",\"%s\")", (item['word'], item['short_exp'], item['long_exp']))
        self.cur.connection.commit()

    def process_item(self, item, spider):
        # 1st Step: drop items whose short_exp and long_exp fields are null
        if ((item['short_exp'] == "") and (item['long_exp'] == "")):
            raise DropItem("no-explanation word found: %s" % item)
        # 2nd Step: drop duplicate items
        elif (item['word'] in self.word_exist):
            raise DropItem("Duplicate word found: %s" % item)
        else:
            self.word_exist.add(item['word'])
            # 3rd Step: save reliable word item to mySQL database
            self.save_to_mysql(item)
            return item
