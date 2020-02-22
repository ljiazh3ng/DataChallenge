# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.spiders import SitemapSpider


class DestiSpider(SitemapSpider):
    name = 'desti'
    # allowed_domains = ['tourist-destinations.com/post-sitemap1.xml']
    sitemap_urls = ['https://www.holidify.com/sitemap.xml']
    sitemap_rules = [('sightseeing-and','parse_places')]

    def parse_places(self, response):
        place = response.url.split('/')[4]
        for dest in response.xpath("//div[@class='card content-card']"):
            yield {
                'place': place,
                'destination':' '.join(dest.xpath(".//h3[@class='card-heading']/text()").extract_first().split(' ')[2:])
                # 'destination': response.xpath(//*[@class='heading2 w-100']/text()).get().replace("")
                # 'title': response.css("title ::text").extract_first(),
                # 'url': response.url
            }
        #def parse(self, response):
        #  with open(destination.csv, 'a+') as f:
        #     yield{
        #     open_in_browser(response)
        #     print(response.xpath("//td/a/@href)").extract_first())
        #     }
        # for url in response.xpath("//td/a/@href"):
        #     yield {
        #         log(url.xpath("//td/a/@href").extract_first())
        #     }
    #     for urls in response.xpath("//td/a/@href"):
    #         print (urls)
    #     return Request(response.url, callback = self.parse_sitemap_url)
    # def parse_sitemap_url(self, response):
    #     print("Hi")
    # do stuff with your sitemap links
