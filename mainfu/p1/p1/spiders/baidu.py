# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.tianyancha.com/company/2995981992']

    def parse(self, response):
        html = Selector(response=response)
        print(html)
        title = html.xpath("//div[@id='_container_baseInfo']").extract()
        print(title)