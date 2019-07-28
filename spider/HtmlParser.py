import random
from bs4 import BeautifulSoup
from spider import Item
import re
from urllib.parse import urlparse


# 对于指定的HTML页面进行解析，抽取出要抓取图片的url和name
# 保存在Item对象中，Item对象保存在一个“线程安全”队列中
# 生产者-消费者模型

class HtmlParser(object):
    '''
    每一个HtmlParser对象中保存了要解析的HTML页面
    parser = HtmlParser(html, taskManager)
    parser.pageUrlParser()
    parser.fileUrlParser()
    '''

    def __init__(self, taskManager):
        # super().__init__()
        self.taskManager = taskManager

    # 解析出新目标页面链接
    def pageUrlParser(self, url, html, threadName):
        path = urlparse(url).path
        id = re.findall(r"[0-9]+", path)[0]
        url = "http://www.tan8.com/yuepu-{}-m.html".format(int(id) + int(threadName) + 1)

        self.taskManager.addPageUrl(url)
        # print('线程' + str(threadName) + 'addPage:' + url)

    # 解析出新文件链接
    def fileUrlParser(self, url, html, threadName):
        # print('线程 ' + str(threadName) + ' 开始解析新图片链接')
        soup = BeautifulSoup(html, 'html.parser')
        try:
            title = (soup.title).string
            imgTags = soup.find('div', class_='swiper-container').find_all('img')
            total = len(imgTags)

            for imgTag in imgTags:
                img = imgTag['src']
                path = urlparse(img).path.split('/')[-1]
                id = urlparse(img).path.split('/')[-2]
                num = int(path.split('.')[-2]) + 1

                item = Item.Item(img, "{0} {1} {2}-{3}" .format(id, title, num, total))
                self.taskManager.addFileItem(item)
        except:
            pass
            # 如果发生异常，说明页面不含有想要的链接，直接跳过继续即可
