# encoding: utf-8
from GetPrice import GetPrice
import time
import sys
import os

class GRID(object):
	def __init__(self):
		self.price = GetPrice()
		
	def generate_grid(self, comp_name):
		try:
			price = self.price.get_price(comp_name)
			grid = {i: 0 for i in range(-10, 11)}
			for i in range(-10, 11):
				grid[i] = (1 + i*0.01)*price
				print("\t%+d%%:\t%.2f\t%+.2f"%(i, grid[i], grid[i]-price))
			for i in range(-10, 11):
				sys.stdout.write("\033[F\r")
		except Exception:
			print("info of the company doesn't exist!")
		
if __name__=='__main__':
	grid = GRID()
	while(1):
		'''
		name = input('Please enter the name of corp:')
		if name == 'q' or name == 'quit' or name == 'exit':
			break
		'''
		name = '歌尔股份'
		grid.generate_grid(name)
		time.sleep(1)
