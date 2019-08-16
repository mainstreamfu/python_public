# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://news.cnblogs.com']

    def parse(self, response):
        html = Selector(response=response)      #创建scrapy对象
        items = html.xpath("//div[@class='content']/h2[@class='news_entry']/a/text()").extract()
        for i in items:
            print(i)


