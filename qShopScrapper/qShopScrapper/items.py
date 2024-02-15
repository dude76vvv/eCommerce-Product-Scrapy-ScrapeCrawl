# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QshopscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class qSwitchGameItem(scrapy.Item):
   title = scrapy.Field()               #title can be incomplete from the card container
   price = scrapy.Field()
   url = scrapy.Field()                 #url product detail page
   description = scrapy.Field()         #go to detail page to get dercriptions
