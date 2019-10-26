from scrapy import Spider, Request
import re
import math

######DUMMY SPIDER
######SPIDER STARTS AT TOP_100_ACTION PAGE
######SPIDER ENTERS PAGE OF EACH OF THE 100 ENTRIES
######SPIDER SCRAPES THE 6 ITEMS FROM ITEMS.PY

class MovieInfo:
    def __init__(self, title, criticscore, audiencescore, rating, boxoffice, runtime):
        self.title = title
        self.criticscore = criticscore
        self.audiencescore = audiencescore
        self.rating = rating
        self.boxoffice = boxoffice
        self.runtime = runtime

class RTSpider(Spider):
    name = 'rt_spider'
    allowed_domains = ['https://www.rottentomatoes.com']
    start_urls = ["/top/bestofrt/top_100_action__adventure_movies/", "/top/bestofrt/top_100_animation_movies/", "/top/bestofrt/top_100_art_house__international_movies/", "/top/bestofrt/top_100_classics_movies/", "/top/bestofrt/top_100_comedy_movies/", "/top/bestofrt/top_100_documentary_movies/", "/top/bestofrt/top_100_drama_movies/", "/top/bestofrt/top_100_horror_movies/", "/top/bestofrt/top_100_kids__family_movies/", "/top/bestofrt/top_100_musical__performing_arts_movies/", "/top/bestofrt/top_100_mystery__suspense_movies/", "/top/bestofrt/top_100_romance_movies/", "/top/bestofrt/top_100_science_fiction__fantasy_movies/", "/top/bestofrt/top_100_special_interest_movies/", "/top/bestofrt/top_100_sports__fitness_movies/", "/top/bestofrt/top_100_television_movies/", "/top/bestofrt/top_100_western_movies/"]



    def parse_movie(self, response):
        # Assume our xpaths only work on our target page
        try:
            title = response.xpath('//div[@id="content"]//h2/text()').extract()
            page  = response.xpath('//span[@class="pageInfo"]/text()').extract()[0]
        except:
            print ("Error in URL: %s" % response.url)
            return

        print ('Title: %s , %s' % (title, page))
        movie_info = set()

        for item in response.xpath('//*[@id="mainColumn"]/section[4]/div/h2'):

            criticscore = response.xpath('//*[@id="tomato_meter_link"]/span[2]').extract()
            audiencescore =
            response.xpath('//*[@id="topSection"]/div[2]/div[1]/section/section/div[2]/h2/a/span[2]').extract()
            rating = response.xpath('//*[@id="mainColumn"]/section[4]/div/div/ul/li[1]/div[2]').extract()
            boxoffice = response.xpath('//*[@id="mainColumn"]/section[4]/div/div/ul/li[7]/div[2]').extract()
            runtime = response.xpath('//*[@id="mainColumn"]/section[4]/div/div/ul/li[8]/div[2]/time').extract()

        m = MovieInfo(title, criticscore, audiencescore, rating, boxoffice, runtime)
        movie_info.add(m)
