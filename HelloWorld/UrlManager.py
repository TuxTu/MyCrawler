# coding:utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return self.new_url_size() != 0

    def get_new_url(self):
        if len(self.new_urls) == 0:
            print("Currently has no url!")
            return
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        if url is None:
            return None
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return 0
        for url in urls:
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.add(url)

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)
