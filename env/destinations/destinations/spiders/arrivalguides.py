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

class ArrivalguidesSpider(SitemapSpider):
    name = 'arrivalguides'
    sitemap_urls = ['https://www.arrivalguides.com/sitemap/xml']
    sitemap_rules = [('essentialinformation','parse_nothing'),('com/en','parse_eng'),('arrivalguides','parse_arr')]

    def parse_nothing(self, response):
        print("Essential Useless Info")

    def parse_eng(self, response):
        if response.xpath("//h1[@class='facts-title']/text()").extract_first() != None:
            loader = MyItemLoader(selector=response)
            loader.add_xpath("destination", "//h1[@class='facts-title']/text()")
            loader.add_xpath("continent", "//div[@class='breadcrumbs-links']/a[1]/text()")
            loader.add_xpath("country", "//div[@class='breadcrumbs-links']/a[2]/text()")
            loader.add_xpath("city", "//div[@class='breadcrumbs-links']/a[3]/text()")
            yield loader.load_item()

    def parse_arr(self, response):
        url = response.url.split('/')
        url[3] = 'en'
        newurl = '/'.join(url)
        yield response.follow(newurl, callback= self.parse_eng)
