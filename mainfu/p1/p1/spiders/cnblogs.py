# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ..items import P1Item


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://news.cnblogs.com']

    def parse(self, response):
        html = Selector(response=response)      #创建scrapy对象
        title = html.xpath("//div[@class='content']/h2[@class='news_entry']/a/text()").extract()
        contents = html.xpath("//div[@class='content']/div[@class='entry_summary']/text()").extract()
        # dic = dict(zip(title,contents))
        # print(dic)
        item_title = P1Item(title=title)
        item_contents = P1Item(contents=contents)


        #特殊写法，这样写就可以直接交给pipelines里的process_item的形参（item, spider）
        yield item_contents,item_title
        # for i in items:
        #     print(i)


