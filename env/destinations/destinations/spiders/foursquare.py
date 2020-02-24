# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.spiders import SitemapSpider

class FoursquareSpider(SitemapSpider):
    name = 'foursquare'
    sitemap_urls = ['https://4sq-sitemap.s3.amazonaws.com/sitemap_index.xml']

    def parse(self, response):
        yield {
            'title': response.css("title ::text").extract_first(),
            'url': response.url
        }
