# 单线程下载，已弃用
# 由MultiThreadFileDownloader取代

import urllib.request
import os

class FileDownloader(object):
    def __init__(self, taskManager):
        super().__init__()
        self.taskManager = taskManager
        self.dirname = '舰队Collection图鉴'
        self.createdir()

    def createdir(self):
        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)

    def download(self):

        # Python不支持 while (item = self.taskManager.getFileItem()) != None 语法
        # Python赋值语句无返回值（Java中赋值语句返回所赋的值）
        item = self.taskManager.getFileItem()
        while item != None:
            url = item.url
            name = item.name
            filePath = self.dirname + os.sep + name + '.jpg'
            urllib.request.urlretrieve(url, filePath)

            item = self.taskManager.getFileItem()

        # while (item = self.taskManager.getFileItem()) != None:
        #     url = item.url
        #     name = item.name
        #     filePath = self.dirname + os.sep + name + '.jpg'
        #     urllib.request.urlretrieve(url, filePath)
