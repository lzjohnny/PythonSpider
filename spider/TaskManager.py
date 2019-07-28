from urllib.parse import urlparse
from spider.Config import LOG_HIDE_HOST
import queue
import threading


# 放入速度 > 取出速度 可以缓冲
# 放入速度 < 取出速度 执行取出行为线程阻塞
# 可选参数1为block=True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。即消费者线程阻塞
# 如果队列为空且block为False，队列将引发Empty异常。
# 可选参数2为timeout=None，如果timeout为非负数，那么线程阻塞最长时间为该值，超时后产生empty exception

# 任务管理器：待下载网页任务、待下载文件任务
# 待下载网页只保存url；待下载文件保存item对象，包含url和文件名
class TaskManager():
    def __init__(self):
        # threading.Thread.__init__(self)
        # Queue为线程安全队列（内置线程锁）
        # Queue()参数maxsize<=0，队列长度无限
        self.fileDownloadTaskQueue = queue.Queue()
        self.pageDownloadTaskQueue = queue.Queue()
        self.s = set()

    def addFileItem(self, item):
        l = threading.Lock()
        l.acquire()
        dup = self.isDuplication(item.url)
        l.release()
        if not dup:
            self.fileDownloadTaskQueue.put(item)
            name = item.name
            url = item.url

            log_url = url
            if LOG_HIDE_HOST:
                log_url = urlparse(url).path
            print('addFile:{0} url:{1}'.format(name, log_url))

    # 取不出元素返回None
    # def get(self):
    #     if self.taskQueue.qsize() != 0:
    #         return self.taskQueue.get(block = False)
    #     else:
    #         return None

    # 取不出元素等待10s
    def getFileItem(self):
        try:
            item = self.fileDownloadTaskQueue.get(timeout=10)
            return item
        except:
            return None

    def addPageUrl(self, url):
        # 检测重复，set非线程安全，需要显式加锁
        l = threading.Lock()
        l.acquire()
        dup = self.isDuplication(url)
        l.release()
        if not dup:
            self.pageDownloadTaskQueue.put(url)

            log_url = url
            if LOG_HIDE_HOST:
                log_url = urlparse(url).path
            print('addPage: ' + log_url)

    def getPageUrl(self):
        try:
            url = self.pageDownloadTaskQueue.get(timeout=10)
            return url
        except:
            return None

    def isDuplication(self, url):
        if url in self.s:
            return True
        self.s.add(url)
        return False
