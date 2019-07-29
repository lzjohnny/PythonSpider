from spider.Config import *
import random
import threading
import time
import urllib.request
import os
from spider.LogInit import log


class MultiThreadFileDownloader(threading.Thread):
    def __init__(self, taskManager, threadName):

        threading.Thread.__init__(self)
        self.taskManager = taskManager
        self.threadName = threadName
        self.dirname = 'downloads'
        self.createdir()

    def createdir(self):
        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)

    def run(self):
        self.download()
        log.info(str(self.threadName) + '线程停止')

    def download(self):
        # Python不支持 while (item = self.taskManager.getFileItem()) != None 语法
        # Python赋值语句无返回值（Java中赋值语句返回所赋的值）
        item = self.taskManager.getFileItem()
        sleepTime = FILE_DL_NORMAL_SLEEP
        while item is not None:
            log.info(str(self.threadName) + '线程当前item：' + str(item))
            url = item.url
            name = item.name

            log.info(str(self.threadName) + '线程当前下载图片：' + name)
            filePath = self.dirname + os.sep + name + '.png'

            remaining_download_tries = DOWNLOAD_TRIES
            while remaining_download_tries > 0:
                try:
                    urllib.request.urlretrieve(url, filePath)
                except:
                    log.info('{0}线程下载图片异常 name:{1} url:{2}'.format(str(self.threadName), name, url))
                    remaining_download_tries = remaining_download_tries - 1
                    continue
                else:
                    break
            item = self.taskManager.getFileItem()

            if random.randint(0, 9) == 0:  # 10% 概率进行下载队列拥挤程度评定
                if self.taskManager.getFileDownloadTaskQueueCount() > QUEUE_CROWDED_SIZE:
                    sleepTime = FILE_DL_SHORT_SLEEP  # 下载加速
                else:
                    sleepTime = FILE_DL_NORMAL_SLEEP  # 下载常速
            time.sleep(sleepTime)
