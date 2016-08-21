import HtmlParser
import TaskManager
import FileDownloader
import MultiThreadFileDownloader
import HtmlPageDownloader
import MultiThreadHtmlPageDownloader

class CoreSpider(object):
    def __init__(self, url, pageDLThreadNum, fileDLThreadNum):
        super().__init__()
        # self.url = url
        self.taskManager = TaskManager.TaskManager()
        self.taskManager.addPageUrl(url)
        self.pageDLThreadNum = pageDLThreadNum
        self.fileDLThreadNum = fileDLThreadNum

    # 待修改
    def start(self):

        # print('开始下载页面')
        # 单线程下载网页
        # pageDownload = HtmlPageDownloader.HtmlPageDownloader(self.url)
        # html = pageDownload.download()

        # 多线程下载网页
        print('开始多线程下载页面...')
        htmlParser = HtmlParser.HtmlParser(self.taskManager)

        pageDLthreadsList = []
        for i in range(self.pageDLThreadNum):
            pageDownloaderThread = MultiThreadHtmlPageDownloader.MultiThreadHtmlPageDownloader(self.taskManager, htmlParser, i)
            pageDLthreadsList.append(pageDownloaderThread)

        # pageDownloader_thread1 = MultiThreadHtmlPageDownloader.MultiThreadHtmlPageDownloader(self.taskManager, htmlParser, 1)
        # pageDownloader_thread2 = MultiThreadHtmlPageDownloader.MultiThreadHtmlPageDownloader(self.taskManager, htmlParser, 2)
        # pageDownloader_thread3 = MultiThreadHtmlPageDownloader.MultiThreadHtmlPageDownloader(self.taskManager, htmlParser, 3)
        # pageDownloader_thread4 = MultiThreadHtmlPageDownloader.MultiThreadHtmlPageDownloader(self.taskManager, htmlParser, 4)
        # pageDownloader_thread5 = MultiThreadHtmlPageDownloader.MultiThreadHtmlPageDownloader(self.taskManager, htmlParser, 5)

        # pageDLthreadsList.append(pageDownloader_thread1)
        # pageDLthreadsList.append(pageDownloader_thread2)
        # pageDLthreadsList.append(pageDownloader_thread3)
        # pageDLthreadsList.append(pageDownloader_thread4)
        # pageDLthreadsList.append(pageDownloader_thread5)

        for t in pageDLthreadsList:
            t.start()
        # print('页面下载完成')

        # print('页面开始解析')
        # htmlParser = HtmlParser.HtmlParser(self.taskManager)
        # htmlParser.parse() #解析后任务会添加到TaskManager队列中
        # print('页面解析完成')

        # 单线程下载图片
        # fileDownloader = FileDownloader.FileDownloader(self.taskManager)
        # fileDownloader.download()

        #多线程下载图片
        # print('开始下载图片')
        fileDLthreadsList = []
        for i in range(self.fileDLThreadNum):
            fileDownloaderThread = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, i)
            fileDLthreadsList.append(fileDownloaderThread)

        # fileDownloader_thread1 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 1)
        # fileDownloader_thread2 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 2)
        # fileDownloader_thread3 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 3)
        # fileDownloader_thread4 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 4)
        # fileDownloader_thread5 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 5)

        # fileDLthreadsList.append(fileDownloader_thread1)
        # fileDLthreadsList.append(fileDownloader_thread2)
        # fileDLthreadsList.append(fileDownloader_thread3)
        # fileDLthreadsList.append(fileDownloader_thread4)
        # fileDLthreadsList.append(fileDownloader_thread5)

        for t in fileDLthreadsList:
            t.start()

        # threading.Thread类的join方法：在子线程完成运行之前，这个子线程的父线程将一直被阻塞
        # 这里为每个子线程都调用了join方法，只有当所有的子线程都执行完毕后，主线程才会继续执行
        for t in fileDLthreadsList:
            t.join()