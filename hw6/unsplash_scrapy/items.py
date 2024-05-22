# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class UnsplashItem(scrapy.Item):
    image_url = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
