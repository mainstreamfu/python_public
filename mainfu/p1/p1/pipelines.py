# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class P1Pipeline(object):
    # def __init__(self):
    #     self.f = f
    def process_item(self, item, spider,):
        # print(item['title'])
        # print(type(item['title']))
        # for i in item['title']:
        #     self.f.write(i+'\n')
        #self.flush()强刷，强行把缓冲区中的内容写到文件中
        # self.flush()
        for i in len(item):
            print(item[i])
        return item


    def open_spider(self,spider):
        '''
        爬虫开始执行时，调用
        :param spider:
        :return:
        '''
        self.f =open('title.log','w',encoding='utf-8')

    def close_spider(self,spider):
        '''
        爬虫关闭时，调用
        :param spider:
        :return:
        '''
        self.close()
