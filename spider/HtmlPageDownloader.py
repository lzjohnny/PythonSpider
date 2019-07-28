# 单线程下载，已弃用
# 由MultiThreadHtmlPageDownloader取代

import urllib.request

# 下载网页
class HtmlPageDownloader(object):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def download(self):
        req = urllib.request.Request(self.url)
        req.add_header('user-agent',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')
        req.add_header('Host', 'www.tan8.com')

        response = urllib.request.urlopen(req)
        if response.getcode() != 200:
            return None
        html = response.read()
        return html