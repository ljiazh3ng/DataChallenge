# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.spiders import SitemapSpider


class DestiSpider(SitemapSpider):
    name = 'holidify'
    sitemap_urls = ['https://www.holidify.com/sitemap.xml']
    sitemap_rules = [('sightseeing-and','parse_places')]

    def parse_places(self, response):
        place = response.url.split('/')[4]
        for dest in response.xpath("//div[@class='card content-card']"):
            yield {
                'place': place,
                'destination':' '.join(dest.xpath(".//h3[@class='card-heading']/text()").extract_first().split(' ')[2:])
            }