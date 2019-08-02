import requests,time
from lxml import etree
from w3lib import html

class Rongyao():
    def __init__(self):
        self.urls="https://www.biqiuge.com"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    def getHtml(self,urls):
        ret= requests.get(self.urls+urls,headers=self.headers)
        ret.encoding = ret.apparent_encoding
        return ret

    def getText(self,text):
        html_ret = etree.HTML(text)
        a_list = html_ret.xpath("//dd//a")
        for item in range(0,2):
            href = a_list[item].get("href")
            html2_ret = self.getHtml(href)
            print(html2_ret)
            html3_ret = etree.HTML(html2_ret.text)
            text = html3_ret.xpath('//div[@id="content"]//text()')
            for item in range(len(text)):
                print(etree.tostring(text[0]))
if __name__=="__main__":
    urls = "/book/36273/"
    rongyao = Rongyao()
    html = rongyao.getHtml(urls)
    text = rongyao.getText(html.text)
