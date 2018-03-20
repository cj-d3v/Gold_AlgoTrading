from goldalgo.execution.optimizer import *

class TWAP(Optimizer):

    _name = 'TWAP'

    def __init__(self):
        super().__init__()

    def get_child_orders(self, timestamp):
        return []

