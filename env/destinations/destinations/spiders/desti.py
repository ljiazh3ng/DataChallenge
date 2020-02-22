# -*- coding: utf-8 -*-
import scrapy


class DestiSpider(scrapy.Spider):
    name = 'desti'
    allowed_domains = ['tourist-destinations.com/post-sitemap1.xml']
    start_urls = ['http://tourist-destinations.com/post-sitemap1.xml/']

    def parse(self, response):
        pass
