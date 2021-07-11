# encoding: utf-8
from HtmlDownloader import HtmlDownloader
from Loader import Loader
from bs4 import BeautifulSoup
import re

class GetPrice(object):
	def __init__(self):
		self.downloader = HtmlDownloader()
		self.loader = Loader()
		self.xueqiu_url = 'https://xueqiu.com/S/'
		self.company_list = self.loader.load_list()

	def get_price(self, comp_name):
		try:
			comp_code = self.company_list[comp_name]
			html = self.downloader.download(self.xueqiu_url+comp_code)	
			soup = BeautifulSoup(html, 'html.parser')
			price = soup.find('div', class_='stock-price').get_text()
			price = price.replace('$', '')
			price = price.replace('¥', '')
			price = re.sub(r'[+|-].*', '', price)
			price = eval(price)
			return price
		except Exception:
			print("get_price: error!")
			return
