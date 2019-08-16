# -*- coding: utf-8 -*-
import scrapy


class AutohomeSpider(scrapy.Spider):
    name = 'autohome'
    allowed_domains = ['autohome.com']
    start_urls = ['http://autohome.com/']

    def parse(self, response):
        print(response.text)
