import os
import sys
from spider.Tools import logger

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from spider import CoreSpider

if __name__ == "__main__":
    # 开始爬虫
    logger.warning("开始爬虫!")

    # 种子链接：导航页面
    url = "http://www.tan8.com/yuepu-10-m.html"

    pageDLThreadNum = 10
    fileDLThreadNum = 10

    spider = CoreSpider.CoreSpider(url, pageDLThreadNum, fileDLThreadNum)
    spider.start()
