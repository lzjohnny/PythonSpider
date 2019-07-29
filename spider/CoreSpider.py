from spider import HtmlParser
from spider import MultiThreadFileDownloader
from spider import MultiThreadHtmlPageDownloader
from spider import TaskManager
from spider.LogInit import log


class CoreSpider(object):
    def __init__(self, url, pageDLThreadNum, fileDLThreadNum):
        super().__init__()
        # self.url = url
        self.taskManager = TaskManager.TaskManager()
        # self.taskManager.pageDownloadTaskQueue.put(url)
        self.taskManager.addPageUrl(url)
        self.pageDLThreadNum = pageDLThreadNum
        self.fileDLThreadNum = fileDLThreadNum

    def start(self):

        # 多线程下载网页
        log.info('开始多线程下载页面...')
        htmlParser = HtmlParser.HtmlParser(self.taskManager)

        pageDLthreadsList = []
        for i in range(self.pageDLThreadNum):
            pageDownloaderThread = MultiThreadHtmlPageDownloader.MultiThreadHtmlPageDownloader(self.taskManager, htmlParser, i)
            pageDLthreadsList.append(pageDownloaderThread)

        for t in pageDLthreadsList:
            t.start()

        #多线程下载图片
        # log.info('开始下载图片')
        fileDLthreadsList = []
        for i in range(self.fileDLThreadNum):
            fileDownloaderThread = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, i)
            fileDLthreadsList.append(fileDownloaderThread)

        for t in fileDLthreadsList:
            t.start()

        # threading.Thread类的join方法：在子线程完成运行之前，这个子线程的父线程将一直被阻塞
        # 这里为每个子线程都调用了join方法，只有当所有的子线程都执行完毕后，主线程才会继续执行
        for t in fileDLthreadsList:
            t.join()
