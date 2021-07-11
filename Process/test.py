# encoding: utf-8
from GetPrice import GetPrice

class Calculator(object):
	def __init__(self):
		self.gp = GetPrice()

	def calculate_percentage(self, corp_name, perc, n):
		buyin_price = self.gp.get_price(corp_name)
		target_price = buyin_price * (1 + perc)
		fees = 0
		tax = target_price * n * 0.1
		if int(buyin_price * n / 100) < 1:
			fees += 5	
		else:
			fees += int(buyin_price * n / 100) * 5
		if int(target_price * n / 100) < 1:
			fees += 5	
		else:
			fees += int(taget_price * n / 100) * 5
		profit = (target_price - buyin_price) * n - fees - tax
		print("Income from this trading:%.2f"%(profit))

if __name__ == '__main__':
	calculator = Calculator()
	while(1):
		name = input('Please input the name of corp:')
		if name == 'q':
			break
		perc = input('Please input the perc you want to sell:')
		if perc == 'q':
			break
		n = input('Please input how many contracts you will buy:')
		if n == 'q':
			break
		calculator.calculate_percentage(name, eval(perc)/100, eval(n))
