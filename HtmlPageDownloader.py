import urllib.request

# 下载网页
class HtmlPageDownloader(object):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def download(self):
        req = urllib.request.Request(self.url)
        req.add_header('user-agent',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0')
        req.add_header('Host', 'zh.moegirl.org')

        response = urllib.request.urlopen(req)
        if response.getcode() != 200:
            return None
        html = response.read()
        return html