import HtmlParser
import TaskManager
import FileDownloader
import MultiThreadFileDownloader
import HtmlPageDownloader

class CoreSpider(object):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.taskManager = TaskManager.TaskManager()

    def start(self):

        print('页面开始下载')
        pageDownload = HtmlPageDownloader.HtmlPageDownloader(self.url)
        html = pageDownload.download()
        print('页面下载完成')

        print('页面开始解析')
        htmlParser = HtmlParser.HtmlParser(html, self.taskManager)
        htmlParser.parse() #解析后任务会添加到TaskManager队列中
        print('页面解析完成')

        # 单线程下载图片
        # fileDownloader = FileDownloader.FileDownloader(self.taskManager)
        # fileDownloader.download()

        #多线程下载图片
        print('开始下载图片')
        fileDownloader_thread1 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 1)
        fileDownloader_thread2 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 2)
        fileDownloader_thread3 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 3)
        fileDownloader_thread4 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 4)
        fileDownloader_thread5 = MultiThreadFileDownloader.MultiThreadFileDownloader(self.taskManager, 5)

        threadsList = []
        threadsList.append(fileDownloader_thread1)
        threadsList.append(fileDownloader_thread2)
        threadsList.append(fileDownloader_thread3)
        threadsList.append(fileDownloader_thread4)
        threadsList.append(fileDownloader_thread5)

        for t in threadsList:
            t.start()

        # threading.Thread类的join方法：在子线程完成运行之前，这个子线程的父线程将一直被阻塞
        # 这里为每个子线程都调用了join方法，只有当所有的子线程都执行完毕后，主线程才会继续执行
        for t in threadsList:
            t.join()