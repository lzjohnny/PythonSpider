# MoeSpider
从萌娘百科舰C页面下载全舰娘图鉴的简易爬虫
最近在进行Android网络框架开发时，需要服务端进行测试，于是学习一下Python+Flask，也顺便做一做Python的爬虫。

##Python版本：

 - Python 3.5

##项目结构：

 - CoreSpider：控制爬虫的整体逻辑，负责调用其他模块
 - HtmlParser：使用BeautifulSoup解析HTML页面，通过对HTML标签及其属性的选择，获取所有目标的名称和链接
 - Item：每一个目标是一个Item对象，包含有url和name属性
 - TaskManager：使用一个线程安全的队列保存任务（下版本将加入多线程支持）
 - FileDownloader：从任务队列中不断取出Item对象，下载并命名、保存到指定位置

##用到的模块

 - 第三方模块 BeautifulSoup
 - 内置模块 urllib.request（在Python2.X版本为urllib2）、queue等

## 需要的改进：增加多线程支持

HtmlParser、FileDownloader和TaskManager构成一个生产者-消费者模型
TaskManager维护一个线程安全队列：放入速度 > 取出速度 可以缓冲，放入速度 < 取出速度 执行取出行为线程阻塞