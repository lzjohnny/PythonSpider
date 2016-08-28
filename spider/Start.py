from spider import CoreSpider

if __name__ == "__main__":
    # 开始爬虫
    print("START!")

    # 种子链接：图鉴页面
    # url = "https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection/%E5%9B%BE%E9%89%B4/%E8%88%B0%E5%A8%98"

    # 种子链接：导航页面
    url = "https://zh.moegirl.org/zh-cn/Template:%E8%88%B0%E9%98%9FCollection:%E5%AF%BC%E8%88%AA"

    pageDLThreadNum = 5
    fileDLThreadNum = 5
    spider = CoreSpider.CoreSpider(url, pageDLThreadNum, fileDLThreadNum)
    spider.start()
