from goldalgo.strategy.template import *

class PFB_Strategy(Strategy):

    _name = 'Portfolio_B'

    def __init__(self):
        super().__init__()
        # init your own states

    def generate_orders(self, config, timestamp):
        return []
