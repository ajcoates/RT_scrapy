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
        top100 = response.xpath('/html/body/div[4]/div[2]/div[1]/section/div/table//@href')
        for selector in top100:
            url = 'https://www.rottentomatoes.com' + selector.extract()
            try:

                yield self.get_movieinfo(url)
            except Exception as e:
                print("Error in '{}' {}".format(url, e))

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
        print("getting movie info for '{}'".format(url))

        content = RTSpider._get_content(url)

        def grab_data(my_xpath):
            return Selector(text=content).xpath(my_xpath).extract()[0].strip()

        return {
            "title": grab_data('//h1[@class="mop-ratings-wrap__title mop-ratings-wrap__title--top"]/text()'),
            "criticscore": grab_data('//*[@id="tomato_meter_link"]/span[2]/text()'),
            "audiencescore": grab_data('//*[@id="topSection"]/div[2]/div[1]/section/section/div[2]/h2/a/span[2]/text()'),
            "rating": grab_data('//*[@id="mainColumn"]/section[4]/div/div/ul/li[1]/div[2]/text()'),
            "boxoffice": grab_data('//*[@id="mainColumn"]/section[4]/div/div/ul/li[7]/div[2]/text()'),
            "runtime": grab_data('//*[@id="mainColumn"]/section[4]/div/div/ul/li[8]/div[2]/time/text()'),
        }
