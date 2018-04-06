import datetime
from goldalgo.orders import *
from goldalgo.execution.scheduler import *
from goldalgo.execution.optimizer import *

class TWAP(Optimizer):

    _name = 'TWAP'

    def __init__(self):
        self._interval = datetime.timedelta(minutes=15)
        self._scheduler = TradeScheduler()

    def execute_strategy_orders(self, config, timestamp, orders):
        """
        for each order in orders
            1. calculate no. of child orders (n) from timestamp and order.endtime
            2. t = timestamp
            3. for i in range(n)
                3.1 calculate child order timestamp (t) t = t + self._interval
                3.2 create chlid order object (c) c.qty = order.qty / n
                    c = ChildOrder(soid, coid, ..., null)
                3.3 self._scheduler.push(t, c)

        """
        pass

    def pop_child_orders(self, timestamp):
        return []

