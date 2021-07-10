from HtmlDownloader import HtmlDownloader
from bs4 import BeautifulSoup

class xqCrawler(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.origin_url = 'https://xueqiu.com/S/'

    def crawl(self, stock_code):
        html = self.downloader.download(self.origin_url+stock_code)
        if html == None:
            return
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.find('div', class_='stock-name').get_text()
        price = soup.find('div', class_='stock-price').get_text()
        print("股票代码:%s,名称为:%s,当前股价:%s"%(stock_code, name, price))

if __name__ == '__main__':
    crawler = xqCrawler()
    for i in range(10000):
        code = 'SZ'+str(i).zfill(6)
        crawler.crawl(code)
