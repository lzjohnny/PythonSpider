import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from spider import CoreSpider

if __name__ == "__main__":
    # 开始爬虫
    print("START!")

    # 种子链接：导航页面
    # url = "http://www.tan8.com/piano.html"
    url = "http://www.tan8.com/yuepu-80-m.html"
    # url = "https://zh.moegirl.org/zh-cn/Template:%E8%88%B0%E9%98%9FCollection:%E5%AF%BC%E8%88%AA"

    pageDLThreadNum = 3
    fileDLThreadNum = 3

    spider = CoreSpider.CoreSpider(url, pageDLThreadNum, fileDLThreadNum)
    spider.start()
