from scrapy import Spider,
from rt_items import scrapy.cfg
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

    def parse(self, response):
        ##### THIS FINDS THE REVIEW PAGES
        # Find the total number of pages in the result so that we can decide how many urls to scrape next
        text = response.xpath('https://www.rottentomatoes.com').extract_first()
        number_pages = 100
        ##### List comprehension to construct all the urls
        result_urls = ['https://www.rottentomatoes.com'.format(x) for x in range(1,number_pages+1)]

    def parse_movie(self, response):
        # Assume our xpaths only work on our target page
        try:
            title = response.xpath('//div[@id="content"]//h2/text()').extract()
            page  = response.xpath('//span[@class="pageInfo"]/text()').extract()[0]
        except:
            print  print "Error in URL: %s" % response.url
            return


    def parse_detail_page(self, response):
        ##### THIS FINDS THE ITEMS DESCRIBED IN ITEMS.PY
        #####

        criticscore = response.xpath('').extract()
        audiencescore = response.xpath('').extract()
        runtime = response.xpath('').extract()
        boxoffice = response.xpath('').extract()
        rating = response.xpath('').extract()
