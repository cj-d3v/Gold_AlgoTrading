from algogold import *

class StrategySelector(object):

	def __init__(self, name):
		self.name = name

	def notify(self, timestamp):
		order = 