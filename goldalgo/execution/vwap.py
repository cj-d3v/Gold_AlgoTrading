from goldalgo.execution.optimizer import *

class VWAP(Optimizer):

    _name = 'VWAP'

    def __init__(self):
        super().__init__()

    def get_child_orders(self, timestamp):
        return []
