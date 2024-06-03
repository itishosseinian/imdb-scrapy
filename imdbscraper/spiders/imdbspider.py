import scrapy
import json
from imdbscraper.items import Info


class ImdbspiderSpider(scrapy.Spider):
    name = "imdbspider"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://m.imdb.com/chart/top/"]

    def parse(self, response):
        
        raw_data = response.css("script[id='__NEXT_DATA__']::text").get()

        json_data = json.loads(raw_data)

        needed_data = json_data['props']['pageProps']['pageData']['chartTitles']['edges']

        information = Info()

        for movie in needed_data:

            
            information['title'] = movie['node']['titleText']['text'],
            information['movie_rank']  = movie['currentRank'],
            information['release_year']  = movie['node']['releaseYear']['year'],
            information['movie_length']  = movie['node']['runtime']['seconds'],
            information['rating']  = movie['node']['ratingsSummary']['aggregateRating'],
            information['vote_count']  = movie['node']['ratingsSummary']['voteCount'],
            information['description']  = movie['node']['plot']['plotText']['plainText']
            
            yield information