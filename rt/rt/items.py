# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RtItem(scrapy.Item):
    title = scrapy.Field()
    film = scrapy.Field()
    criticscore = scrapy.Field()
    audiencescore = scrapy.Field()
    runtime = scrapy.Field()
    boxoffice = scrapy.Field()
    rating = scrapy.Field()
