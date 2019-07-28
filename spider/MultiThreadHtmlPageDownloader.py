from urllib.parse import urlparse
from spider.Config import PAGE_DL_SLEEP, LOG_HIDE_HOST
import time
import urllib.request
import threading


# 多线程下载网页
class MultiThreadHtmlPageDownloader(threading.Thread):
    def __init__(self, taskManager, htmlParser, threadName):
        threading.Thread.__init__(self)
        self.taskManager = taskManager
        self.htmlParser = htmlParser
        self.threadName = threadName

    def run(self):
        self.download()

    def download(self):
        url = self.taskManager.getPageUrl()
        while url != None:
            print('线程 ' + str(self.threadName) + ' 开始下载页面')

            req = urllib.request.Request(url)
            req.add_header('user-agent',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0')
            req.add_header('Host', 'www.tan8.com')

            response = urllib.request.urlopen(req)
            if response.getcode() != 200:
                return None
            html = response.read()
            print('--1--')
            self.htmlParser.pageUrlParser(url, html, self.threadName)
            print('--2--')
            self.htmlParser.fileUrlParser(url, html, self.threadName)
            print('--3--')

            url = self.taskManager.getPageUrl()
            log_url = url
            if LOG_HIDE_HOST:
                log_url = urlparse(url).path
            print('取出新页面：' + log_url)

            time.sleep(PAGE_DL_SLEEP)
