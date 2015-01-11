# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HWItem(scrapy.Item):
    webshop = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    #image_urls = scrapy.Field()
    #images = scrapy.Field()
    
class HWPhoneItem(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    
