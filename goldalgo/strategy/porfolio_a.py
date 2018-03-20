from goldalgo.strategy.template import *

class PFA_Strategy(Strategy):
    
    _name = 'Portfolio_A'
    
    def __init__(self):
        super().__init__()
        # init your own state

    def generate_orders(self, timestamp):
        self.current_timestamp = timestamp
        return []
