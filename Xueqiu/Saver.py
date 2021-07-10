# coding: utf-8
import numpy as np
import re

class Saver(object):
    def __init__(self):
        self.file_name = 'A-share_list.npy'
        self.stock_list = {}

    def store_data(self, name, code):
        name.replace('*', '')
        re.sub(r'\(.*', '', name)
        self.stock_list[name] = code

    def output_data(self):
        np.save(self.file_name, self.stock_list)
