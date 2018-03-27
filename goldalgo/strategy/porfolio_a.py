from goldalgo.strategy.template import *

class PFA_Strategy(Strategy):
    
    _name = 'Portfolio_A'
    
    def __init__(self):
        super().__init__()
        # init your own states

    def generate_orders(self, config, timestamp):
        return []
