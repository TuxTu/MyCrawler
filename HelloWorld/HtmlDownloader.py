# coding:utf-8
import requests
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code==200:
            r.encoding='utf-8'
            return r.text
        return None
