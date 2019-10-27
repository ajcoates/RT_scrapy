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

    soft_failures = 0
    hard_failures = 0

    def parse(self, response):
        top100 = response.xpath('/html/body/div[4]/div[2]/div[1]/section/div/table//@href')
        for selector in top100:
            url = 'https://www.rottentomatoes.com' + selector.extract()
            try:
                yield self.get_movieinfo(url)
            except IndexError as ie:
                print("Ignoring error in '{}': '{}'.".format(url, ie))

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
        print("Getting movie info for '{}'".format(url))

        content = RTSpider._get_content(url)

        def make_xpath(sibling_value):
            return '//div[@class="meta-label subtle" and text()="{}: "]/following-sibling::div/text()'.format(sibling_value)

        def grab_data(name, my_xpath, force=False):
            def print_failures(is_hard):
                print("\n{} fail to xpath '{}'!! '{}'. \nsoft fails: {}, hard_fails: {}\n".format(
                    "\tHARD" if is_hard else "Soft", name, my_xpath, self.soft_failures, self.hard_failures))

            try:
                return Selector(text=content).xpath(my_xpath).extract()[0].strip()
            except Exception as e:
                if force:
                    self.soft_failures += 1
                    print_failures(False)
                    return None

                self.hard_failures += 1
                print_failures(True)
                raise e

        return {
            "title": grab_data("title", '//h1[@class="mop-ratings-wrap__title mop-ratings-wrap__title--top"]/text()'),
            "criticscore": grab_data("criticscore", '//*[@id="tomato_meter_link"]/span[2]/text()'),
            "criticcount": grab_data("critic count", '//small[@class="mop-ratings-wrap__text--small"]/text()'),
            "audiencescore": grab_data("audiencescore", '//*[@id="topSection"]/div[2]/div[1]/section/section/div[2]/h2/a/span[2]/text()'),
            "audiencevotercount": grab_data("audience score count", '//strong[@class="mop-ratings-wrap__text--small"]/text()'),
            "rating": grab_data("rating", make_xpath("Rating")),
            "boxoffice": grab_data("boxoffice", make_xpath("Box Office"), True),
            "runtime": grab_data("runtime", make_xpath("Runtime")),
        }
