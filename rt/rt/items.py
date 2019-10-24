# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RtItem(scrapy.Item):
    film = scrapy.Field()
    rank = scrapy.Field()
    num_reviews = scrapy.Field()
    
    pass
