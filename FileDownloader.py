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

        # python 不支持 while (item = self.taskManager.get()) != None 语法？
        item = self.taskManager.get()
        while item != None:
            url = item.url
            name = item.name
            filePath = self.dirname + os.sep + name + '.jpg'
            urllib.request.urlretrieve(url, filePath)

            item = self.taskManager.get()

        # while (item = self.taskManager.get()) != None:
        #     url = item.url
        #     name = item.name
        #     filePath = self.dirname + os.sep + name + '.jpg'
        #     urllib.request.urlretrieve(url, filePath)
