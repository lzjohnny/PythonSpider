import os
import sys
from spider.LogInit import log

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from spider import CoreSpider

if __name__ == "__main__":
    # 开始爬虫
    log.info("开始爬虫!")

    # 萌百爬虫种子链接：舰C导航页面
    # url = "https://zh.moegirl.org/zh-cn/Template:%E8%88%B0%E9%98%9FCollection:%E5%AF%BC%E8%88%AA"
    # 弹吧爬虫种子链接：首个乐谱页面
    url = "http://www.tan8.com/yuepu-10-m.html"

    pageDLThreadNum = 10
    fileDLThreadNum = 10

    spider = CoreSpider.CoreSpider(url, pageDLThreadNum, fileDLThreadNum)
    spider.start()
