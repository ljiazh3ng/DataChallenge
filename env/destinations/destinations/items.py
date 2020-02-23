# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
class DestinationsItem(scrapy.Item):
    # Primary fields
    continent = Field()
    country = Field()
    city = Field()
    # Log fields
    url = Field()
    date = Field()
