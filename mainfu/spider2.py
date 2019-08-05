import requests
from lxml import html
import os

etree = html.etree
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# 修改book可爬取其他小说
book = '/54840'
# 修改baseDir改变根文件夹
baseDir = '/home/opengwe/Desktop/Books'
domain = 'https://www.biqiuge.com'

def getText(url):
    res = requests.get(url, headers)
    res.encoding = res.apparent_encoding
    return res.text

def getElements(text, xpath):
    html = etree.HTML(text)
    return html.xpath(xpath)

def mkDir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def savePage(novelName, chapter, contents):
    folder = '{}/{}'.format(baseDir, novelName)
    mkDir(folder)
    file = '{}/{}.txt'.format(folder, chapter)
    f = open(file, 'wb')
    for paragraph in contents:
        f.write(bytes(paragraph + '\r\n', 'utf8'))
    f.close()

if __name__ == '__main__':
    novelText = getText(domain + '/book' + book)
    novelName = getElements(novelText, '//div[@class="info"]/h2/text()')[0]
    chapters = getElements(novelText, '//div[@class="listmain"]//dt[2]/following-sibling::dd/a/@href')
    for idx in range(len(chapters)):
        text = getText(domain + chapters[idx])
        contents = [ paragraph.replace(u'\u3000', u' ') for paragraph in getElements(text, '//div[@id="content"]/text()') ]
        chapter = getElements(text, '//div[@class="content"]/h1/text()')[0]
        savePage(novelName, chapter, contents[:-4])
        print('已完成 %s %s' % (novelName, chapter))