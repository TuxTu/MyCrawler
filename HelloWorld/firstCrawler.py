from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader 
from HtmlParser import HtmlParser 
from UrlManager import UrlManager

class firstCrawler(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print("Seized %s links"%self.manager.old_url_size())
            except Exception:
                print("Crawl failed!")
        self.output.output_html()

if __name__=="__main__":
    crawler = firstCrawler()
    print("start...................")
    crawler.crawl("http://baike.baidu.com/view/284853.htm")
