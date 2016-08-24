class Item(object):
    def __init__(self, url, name):
        super().__init__()
        self._url = url
        self._name = name

    @property
    def url(self):
        return self._url()

    @property
    def name(self):
        return self._name

    @url.setter
    def url(self, value):
        self._url = value

    @name.setter
    def name(self, value):
        self._name = value

    @url.getter
    def url(self):
        return self._url

    @name.getter
    def name(self):
        return self._name
    # 如需要使用新属性可以继续添加