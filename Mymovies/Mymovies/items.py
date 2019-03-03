# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MymoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    other_name = scrapy.Field()
    cover_pic = scrapy.Field()
    type = scrapy.Field()
    show_date = scrapy.Field()
    region = scrapy.Field()
    show_year = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    douban_score = scrapy.Field()
    link1 = scrapy.Field()
    link2 = scrapy.Field()
    #pass
