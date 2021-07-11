# encoding: utf-8
class Loader(obejct):
	def load_list(self):
		fo = open('A_share_list', 'r')
		return eval(fo.read())
