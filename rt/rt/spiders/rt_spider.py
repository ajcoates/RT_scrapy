class RTSpider(Spider):
    name = 'rt_spider'
    allowed_domains = ['https://www.rottentomatoes.com']
    start_urls = ['https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/']
    def parse(self, response):
        pass


def parse(self, response):
    # Find the total number of pages in the result so that we can decide how many urls to scrape next
    text = response.xpath('https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/').extract_first()
    _, per_page, total = map(lambda x: int(x), re.findall('\d+', text))
    number_pages = 100
    # List comprehension to construct all the urls
    result_urls = ['https://www.bestbuy.com/site/all-laptops/pc-laptops/pcmcat247400050000.c?cp={}&id=pcmcat247400050000'.format(x) for x in range(1,number_pages+1)]
