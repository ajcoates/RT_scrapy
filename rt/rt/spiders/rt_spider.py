from scrapy import Spider, Selector
import requests
import random
import re
import math
import time

######DUMMY SPIDER
######SPIDER STARTS AT TOP_100_ACTION PAGE
######SPIDER ENTERS PAGE OF EACH OF THE 100 ENTRIES
######SPIDER SCRAPES THE 6 ITEMS FROM ITEMS.PY

class MovieInfo:
    rate = 1
    def __init__(self, criticscore, audiencescore, rating, boxoffice, runtime):
        self.criticscore = criticscore
        self.audiencescore = audiencescore
        self.rating = rating
        self.boxoffice = boxoffice
        self.runtime = runtime

class RTSpider(Spider):
    name = 'rt_spider'
    allowed_domains = ['https://www.rottentomatoes.com']
    start_urls = ["https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_art_house__international_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_classics_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_comedy_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_drama_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_horror_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_kids__family_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_musical__performing_arts_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_mystery__suspense_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_romance_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_science_fiction__fantasy_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_special_interest_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_sports__fitness_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_television_movies/",
                  "https://www.rottentomatoes.com/top/bestofrt/top_100_western_movies/"]

    def parse(self, response):
        genres = response.xpath('//*[@id="mainColumn"]/section[4]/div/h2')
        genre_movies = set()
        print("you are in parse '{}'".format(genres))
        time.sleep(100)
        for item in genres:
            try:
           ## collect item and yield item
                print(item)
            except Error as e:
                print("Error in URL {}".format(e))

    @staticmethod
    def _get_content(link):
        """
        Politely request the page content at link.
        """

        content = requests.get(link).text

        x = 3 + 2 * random.random()
        time.sleep(x)

        return content

    def get_movieinfo(self, url):
        response = None
        genre_movies = set()

        criticscore = response.xpath(
            '//*[@id="tomato_meter_link"]/span[2]').extract()
        audiencescore = response.xpath(
            '//*[@id="topSection"]/div[2]/div[1]/section/section/div[2]/h2/a/span[2]').extract()
        rating = response.xpath(
            '//*[@id="mainColumn"]/section[4]/div/div/ul/li[1]/div[2]').extract()
        boxoffice = response.xpath(
            '//*[@id="mainColumn"]/section[4]/div/div/ul/li[7]/div[2]').extract()
        runtime = response.xpath(
            '//*[@id="mainColumn"]/section[4]/div/div/ul/li[8]/div[2]/time').extract()

        m = MovieInfo(criticscore, audiencescore, rating, boxoffice, runtime)
        genre_movies.add(m)
