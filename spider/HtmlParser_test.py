from bs4 import BeautifulSoup
from bs4 import element
from spider import Item
from spider import HtmlPageDownloader

import urllib

# 初始链接为图鉴页面，仅fileUrlParser方法起到作用
# url = 'https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection/%E5%9B%BE%E9%89%B4/%E8%88%B0%E5%A8%98'
# 测试使用

# 解析出新页面链接
def pageUrlParser(self, html):
    print('开始解析新页面链接')
    pass

# 解析出新目标文件链接
def fileUrlParser(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = (soup.title).string
    name = ((title.split(':'))[1].split(' '))[0]
    tbSet = soup.find_all('table', class_='mw-collapsible mw-collapsed wikitable')
    # 找到含有'图鉴、立绘'关键字的表格
    # 但使用test='图鉴、立绘'属性无效，原因不明
    tbTagTarget = None
    for tbTag in tbSet:
        thTag = tbTag.find('th')
        # print(thTag.contents[0])
        # print(type(thTag.contents[0]))
        # print(len(thTag))
        # if thTag.string != None and (('图鉴、立绘' in thTag.string) or ('圖鑑、立繪' in thTag.string)):
        if thTag.contents[0] != None and (('图鉴、立绘' in thTag.contents[0]) or ('圖鑑、立繪' in thTag.contents[0])):
            print(thTag.contents[0])
            tbTagTarget = tbTag
            break
    trTag = tbTagTarget.contents[3]
    imgTagSet = trTag.find_all('img')
    num = 0  # num为图鉴文件名编号
    for imgTag in imgTagSet:
        srcset = imgTag.get('srcset', None)
        if srcset == None:
            url = imgTag.get('src', None)
            num = num + 1
            # src加入待下载文件队列
            print('addFile:' + name)
            print(url)
        # 如果发生异常，说明页面不含有想要的链接，直接跳过继续即可

url = 'https://zh.moegirl.org/zh-tw/%E8%88%B0%E9%98%9FCollection:%E9%85%92%E9%9F%B5'

# 下载
d = HtmlPageDownloader.HtmlPageDownloader(url)
html_page = d.download()

fileUrlParser(html_page)