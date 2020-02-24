# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.spiders import SitemapSpider
from scrapy.http import HtmlResponse
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst
from scrapy.loader import ItemLoader
clean_text = Compose(MapCompose(lambda v: v.strip()), Join()) 

class MyItemLoader(ItemLoader):
    default_item_class = dict
    continent = clean_text
    country = clean_text
    city = clean_text 
    destination = clean_text

class LonelyplanetSpider(SitemapSpider):
    name = 'lonelyplanet'
    sitemap_urls = ['https://www.lonelyplanet.com/sitemaps/dotcom-sitemaps/destinations_1.xml']

    def parse(self, response):
        for dest in response.xpath("//*[@id='attractions']/div/article/ol"):
            loader = MyItemLoader(selector=response)
            loader.add_value("destination", dest.xpath(".//h5[@class= 'jsx-158429263 responsive-medium leading-tight']/text()").extract_first())
            loader.add_xpath("country", "//*[@id='__next']/div/div[2]/header/div/div[1]/p[1]/a/text()")
            yield loader.load_item()