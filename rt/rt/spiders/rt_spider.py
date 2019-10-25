from scrapy import Spider, Request
from Rt_Items import scrapy.cfg
import re
import math

######DUMMY SPIDER
######SPIDER STARTS AT TOP_100_ACTION PAGE
######SPIDER ENTERS PAGE OF EACH OF THE 100 ENTRIES
######SPIDER SCRAPES THE 6 ITEMS FROM ITEMS.PY

class RTSpider(Spider):
    name = 'rt_spider'
    allowed_domains = ['https://www.rottentomatoes.com']
    start_urls = ['https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/']


    def parse_movie(self, response):
        # Assume our xpaths only work on our target page
        try:
            title = response.xpath('//div[@id="content"]//h2/text()').extract()
            page  = response.xpath('//span[@class="pageInfo"]/text()').extract()[0]
        except:
            print "Error in URL: %s" % response.url
            return

        print 'Title: %s , %s' % (title, page)
        movie_info = set()

        for item in response.xpath('//*[@id="mainColumn"]/section[4]/div/h2')
        ##### THIS FINDS THE ITEMS DESCRIBED IN ITEMS.PY
        #####

        criticscore = response.xpath('//*[@id="tomato_meter_link"]/span[2]').extract()
        audiencescore = response.xpath('//*[@id="topSection"]/div[2]/div[1]/section/section/div[2]/h2/a/span[2]').extract()
        rating = response.xpath('//*[@id="mainColumn"]/section[4]/div/div/ul/li[1]/div[2]').extract()
        boxoffice = response.xpath('//*[@id="mainColumn"]/section[4]/div/div/ul/li[7]/div[2]').extract()
        runtime = response.xpath('//*[@id="mainColumn"]/section[4]/div/div/ul/li[8]/div[2]/time').extract()

        movie_info.append(criticscore, audiencescore, rating, boxoffice, runtime)

    item = movie_zz
###############################################################################################################################################################################################################################################################################################################################################
################
################ SAMPLE CODE FROM THE INTERNET, BELOW; FOR REFERENCE
################

import scrapy

# movies.item is a class that you have to write
from movies.items import MoviesItem

# Library for crawling rules
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class MovieSpider(CrawlSpider):
    name = "movie"                                      # Must be unique
    allowed_domains = ["www.rottentomatoes.com"]        # Restrict spiders to a certain domain
    start_urls = [
        "http://www.rottentomatoes.com/top/bestofrt/?year=2014",    # Where the first spider starts
    ]


        rules = (
        Rule(SgmlLinkExtractor(allow=('http:\/\/www\.rottentomatoes\.com\/m\/\w+\/$', ), ), follow=True),
        Rule(SgmlLinkExtractor(allow=('\/m\/\w+\/reviews\/$', )), callback='parse_movie', follow=True),
        Rule(SgmlLinkExtractor(allow=('\/m\/\w+\/reviews\/\?page=\d+$', )), callback='parse_movie', follow=True),
    )

    # This function scrapes information from a page
    def parse_movie(self, response):
        # Assume our xpaths only work on our target page
        try:
            title = response.xpath('//div[@id="content"]//h2/text()').extract()
            page  = response.xpath('//span[@class="pageInfo"]/text()').extract()[0]
        except:
            print "Error in URL: %s" % response.url
            return


        print 'Title: %s , %s' % (title, page)
        reviews = set()

        # When we hit the appropriate page, try to scrape the review from each table row
        for sel in response.xpath('//div[@id="reviews"]//table//tr'):
            # The content of the review
            review = sel.xpath('.//p/text()').extract()[0]

            # Is this review positive or negative?
            if sel.xpath('.//td//div[contains(@class,"fresh")]'):
                rating = 'fresh'
            elif sel.xpath('.//td//div[contains(@class,"rotten")]'):
                rating = 'rotten'

            reviews.add((rating, review))

        # Push the scraped data into the datastructure we've written
        item = MoviesItem()
        item['title'] = title
        item['reviews'] = list(reviews)
        item['page'] = page

        yield item
