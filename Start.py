import CoreSpider

if __name__ == "__main__":
    # 开始爬虫
    print("START!")
    # 原始链接：图鉴页面
    url = "https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection/%E5%9B%BE%E9%89%B4/%E8%88%B0%E5%A8%98"
    spider = CoreSpider.CoreSpider(url)
    spider.start()
