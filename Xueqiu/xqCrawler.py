from HtmlDownloader import HtmlDownloader
from Saver import Saver
from bs4 import BeautifulSoup

class XqCrawler(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.saver = Saver()
        self.origin_url = 'https://xueqiu.com/S/'

    def crawl(self, stock_code):
        html = self.downloader.download(self.origin_url+stock_code)
        if html == None:
            return
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.find('div', class_='stock-name').get_text()
        price = soup.find('div', class_='stock-price').get_text()
        self.saver.store_data(name, stock_code)
        print("股票代码:%s,名称为:%s,当前股价:%s"%(stock_code, name, price))

if __name__ == '__main__':
    crawler = XqCrawler()
    for i in range(3817):
        code = 'SZ'+str(i).zfill(6)
        crawler.crawl(code)
    for i in range(4000):
        code = 'SH60'+str(i).zfill(4)
        crawler.crawl(code)
    crawler.saver.output_data()
