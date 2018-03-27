from goldalgo.execution.optimizer import *

class TWAP(Optimizer):

    _name = 'TWAP'

    def __init__(self):
        super().__init__()

    def execute_strategy_orders(self, config, timestamp, orders):
        pass

    def pop_child_orders(self, timestamp):
        return []

