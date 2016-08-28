from bs4 import BeautifulSoup
from bs4 import element
from spider import Item
import traceback

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
    def pageUrlParser(self, html, threadName):
        soup = BeautifulSoup(html, 'html.parser')
        tbTag = (soup.find_all('table', class_='nowraplinks mw-collapsible mw-uncollapsed navbox-subgroup'))[0]
        aTagSet = tbTag.find_all('a')

        for aTag in aTagSet[1::]:
            url = aTag.get('href', None)
            if url != None:
                url = 'https://zh.moegirl.org' + url
                self.taskManager.addPageUrl(url)
                # print('线程' + str(threadName) + 'addPage:' + url)

    # 解析出新文件链接
    def fileUrlParser(self, html, threadName):
        # print('线程 ' + str(threadName) + ' 开始解析新图片链接')
        soup = BeautifulSoup(html, 'html.parser')
        try:
            title = (soup.title).string
            name = ((title.split(':'))[1].split(' '))[0]
            tbSet = soup.find_all('table', class_='mw-collapsible mw-collapsed wikitable')
            # 找到含有'图鉴、立绘'关键字的表格
            # 但使用test='图鉴、立绘'属性无效，原因不明
            tbTagTarget = None
            for tbTag in tbSet:
                thTag = tbTag.find('th')
                # if thTag.string != None and (('图鉴、立绘' in thTag.string) or ('圖鑑、立繪' in thTag.string)):
                if thTag.contents[0] != None and (('图鉴、立绘' in thTag.contents[0]) or ('圖鑑、立繪' in thTag.contents[0])):
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
                    item = Item.Item(url, name + '(' + str(num) + ')')
                    self.taskManager.addFileItem(item)
                    # print('线程' + str(threadName) + 'addFile:' + name)
        except:
            pass
            # 如果发生异常，说明页面不含有想要的链接，直接跳过继续即可



