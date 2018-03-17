class StrategyOrder(object):

	def __init__(self, so_id, project_id, portfolio, timestamp, symbol, qty, start_time, end_time, limit_price):

		self.so_id = so_id
		self.project_id = project_id
		self.timestamp = timestamp
		self.symbol = symbol
		self.qty = qty
		self.start_time = start_time
		self.end_time = end_time
		self.limit_price = limit_price 