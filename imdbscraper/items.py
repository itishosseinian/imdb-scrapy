# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Info(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    movie_rank = scrapy.Field() 
    release_year = scrapy.Field() 
    movie_length = scrapy.Field() 
    rating = scrapy.Field() 
    vote_count = scrapy.Field() 
    description = scrapy.Field()    



