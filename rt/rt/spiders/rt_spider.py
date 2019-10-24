class RTSpider(Spider):
    name = 'rt_spider'
    allowed_domains = ['https://www.rottentomatoes.com']
    start_urls = ['https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/']
    def parse(self, response):
        pass
