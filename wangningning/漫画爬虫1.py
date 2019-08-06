import requests,urllib,os
from lxml import etree
from docx import Document
from docx.shared import Inches

class Killdraw():
    def __init__(self):
        self.url = "http://www.4399dmw.com"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def getHtml(self,urls):
        ret = requests.get(self.url+urls,headers=self.headers)
        ret.encoding = ret.apparent_encoding
        return ret

    def getText(self,text):
        html = etree.HTML(text)
        ul = html.xpath('//ul[@class="listing__free-list"]')[0]
        html1 = etree.HTML(etree.tostring(ul).decode("utf-8"))
        href_list = html1.xpath('//li//a//@href')

        x=1
        for href in href_list:
            ret = self.getHtml(href)
            html = etree.HTML(ret.text)
            a_list = html.xpath('//ul[@class="list clearfix"]//li//img//@data-src')
            document = Document()
            for a in a_list:
                img_name = a.rsplit("/",maxsplit=1)[1]
                urllib.request.urlretrieve(a,img_name)
                document.add_picture(img_name,width=Inches(6),height=Inches(10))
                document.save('D://pic/杀行者第%s章.doc'%x)
                os.remove(img_name)

               # doc =
                #ret = requests.get(a)
                #self.writeFile(ret.content,str(x))
        x+=1

    def writeFile(self,content,x):
        with open(r'D:\杀行者第%s.md'%x, 'wb') as f:
            f.write(content)







if __name__=="__main__":
    urls = "/mh/shadaoxz/"
    kd = Killdraw()
    ret = kd.getHtml(urls)
    kd.getText(ret.text)
