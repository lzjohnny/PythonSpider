import random
from spider.Config import PAGE_DL_SLEEP, DOWNLOAD_TRIES
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
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0'
        ]

    def run(self):
        self.download()

    def download(self):
        url = self.taskManager.getPageUrl()
        while url is not None:
            print('线程 ' + str(self.threadName) + ' 开始下载页面')

            req = urllib.request.Request(url)
            ua = random.choice(self.user_agent_list)
            req.add_header('user-agent', ua)
            req.add_header('Host', 'www.tan8.com')

            response = None
            remaining_download_tries = DOWNLOAD_TRIES
            while remaining_download_tries > 0:
                try:
                    response = urllib.request.urlopen(req)
                except:
                    print('{0}线程下载页面异常 url:{1}'.format(str(self.threadName), url))
                    remaining_download_tries = remaining_download_tries - 1
                    continue
                else:
                    break

            if response.getcode() != 200:
                return None
            html = response.read()
            print('--1--')
            self.htmlParser.pageUrlParser(url, html, self.threadName)
            print('--2--')
            self.htmlParser.fileUrlParser(url, html, self.threadName)
            print('--3--')

            url = self.taskManager.getPageUrl()
            print('取出新页面：' + url)

            time.sleep(PAGE_DL_SLEEP)
