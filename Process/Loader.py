# encoding: utf-8
class Loader(object):
	def load_list(self):
		fo = open('A_share_list', 'r')
		dict_ = eval(fo.read())
		fo.close()
		return dict_
