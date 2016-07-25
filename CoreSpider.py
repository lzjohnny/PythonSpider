from bs4 import BeautifulSoup
import urllib.request
import HtmlParser
import TaskManager
import FileDownloader


class CoreSpider(object):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.taskManager = TaskManager.TaskManager()

    def start(self):
        request = urllib.request.Request(self.url)
        request.add_header('user-agent',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0')
        request.add_header('Host', 'zh.moegirl.org')

        response = urllib.request.urlopen(request)
        if response.getcode() != 200:
            return None
        html = response.read()
        # print(html)

        parser = HtmlParser.HtmlParser(html, self.taskManager)
        parser.parse() #解析后任务会添加到TaskManager队列中

        downloader = FileDownloader.FileDownloader(self.taskManager)
        downloader.download()
