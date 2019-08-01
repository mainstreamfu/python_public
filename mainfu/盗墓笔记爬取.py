import requests,os
from bs4 import BeautifulSoup
from bs4.element import NavigableString

def bookSpider(beginDown,endDown,urls,headers,paths):
    session = requests.session()
    session.headers = headers
    ret = session.get(url=urls)
    ret.encoding = ret.apparent_encoding
    soup = BeautifulSoup(ret.text, 'html.parser')
    div = soup.find(name='div', class_='clearfix dirconone')
    li_list = div.find_all(name='li')
    tip = 0
    for li in li_list:
        tip +=1
        if tip >= beginDown+1:
            src = li.find(name="a").get("href")
            ret1 = requests.get(url=src)
            ret1.encoding = ret.apparent_encoding
            soup1 = BeautifulSoup(ret1.text, 'html.parser')
            div = soup1.find(name='div', class_='mainContenr')
            title = soup1.find(name='strong', class_='l jieqi_title').text
            print(title)
            path = paths
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/{}.txt'.format(title)
            for ele in div:
                if type(ele) == NavigableString:
                    content = ele.strip()
                    with open(file_path, 'a', encoding='utf-8') as f:
                        f.write(content + "\n")
        if endDown+1==tip:
            break

if __name__ == "__main__":
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
    url = 'http://www.quanshuwang.com/book/9/9055'
    paths = 'D:/小说'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36', }
    bookSpider(beginDown,endDown,url,headers,paths)


