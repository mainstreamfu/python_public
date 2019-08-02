import requests,os
from lxml import etree


class Rongyao():
    def __init__(self):
        self.urls="https://www.biqiuge.com"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    def getHtml(self,urls):
        ret= requests.get(self.urls+urls,headers=self.headers)
        ret.encoding = ret.apparent_encoding
        return ret

    def loadPath(self,path):
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def getText(self,text,beginDown,endDown):
        html_ret = etree.HTML(text)
        a_list = html_ret.xpath("//dd//a")
        for item in range(beginDown+6,endDown+7):
            title = a_list[item].text
            print('开始下载%s'%title)
            href = a_list[item].get("href")
            html2_ret = self.getHtml(href)
            html3_ret = etree.HTML(html2_ret.text)
            text = html3_ret.xpath('//div[@id="content"]//text()')
            files = path + title +'.md'
            i = 0
            for item in text:
                i += 1
                with open(files, 'a', encoding='utf-8') as f:
                    f.write(item.strip() + "\n")
                if i > len(text) - 4:
                    break
        return print("over")

if __name__=="__main__":
    beginDown = input("请输入爬取的起始章节（整数）：")
    while True:
        if beginDown.isdigit():
            beginDown = int(beginDown)
            if beginDown <= 0:
                beginDown = 1
                break
            else:
                beginDown = int(beginDown)
                break
        else:
            beginDown = input("请输入爬取的起始章节（整数）：")
    endDown = int(input("请输入爬取终止章节："))
    path = 'D:/笔趣阁/'
    urls = "/book/36273/"
    rongyao = Rongyao()
    down = rongyao.loadPath(path)
    html = rongyao.getHtml(urls)
    text = rongyao.getText(html.text,beginDown,endDown)