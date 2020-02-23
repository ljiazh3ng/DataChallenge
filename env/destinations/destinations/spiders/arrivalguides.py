# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.spiders import SitemapSpider
from scrapy.http import HtmlResponse


class ArrivalguidesSpider(SitemapSpider):
    name = 'arrivalguides'
    sitemap_urls = ['https://www.arrivalguides.com/sitemap/xml']
    sitemap_rules = [('essentialinformation','parse_nothing'),('com/en','parse_eng'),('arrivalguides','parse_arr')]

    def parse_nothing(self, response):
        print("Essential Useless Info")

    def parse_eng(self, response):
        if response.xpath("//h1[@class='facts-title']/text()").extract_first() != None:
            yield {
                'title': response.xpath("//h1[@class='facts-title']/text()").extract_first(),
                'url': response.url 
            }

    def parse_arr(self, response):
        url = response.url.split('/')
        url[3] = 'en'
        newurl = '/'.join(url)
        yield response.follow(newurl, callback= self.parse_eng)
