# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UdemyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = Field()
    title = scrapy.Field()
    id = scrapy.Field()
    instructors = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    source = scrapy.Field()


class UdacityItem(scrapy.Item):
    title = scrapy.Field()
    id = scrapy.Field()
    instructors = scrapy.Field()
    level = scrapy.Field()
    prerequisites = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    source = scrapy.Field()

