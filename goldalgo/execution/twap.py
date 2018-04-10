import datetime
from goldalgo.orders import *
from goldalgo.execution.scheduler import *
from goldalgo.execution.optimizer import *

class TWAP(Optimizer):

    _name = 'TWAP'

    def __init__(self):
        self._interval = datetime.timedelta(minutes=5)
        self._scheduler = TradeScheduler()

    def execute_strategy_orders(self, config, timestamp, orders):

        timedelta = config.get_heartbeat()

        for order in orders:

            soid = order.get_soid()
            trade_time = timestamp + timedelta
            symbol = order.get_symbol()
            action = order.get_action()
            qty_left = order.get_qty()
            endtime = order.get_endtime()

            # calculate no. of child orders
            n = int((endtime - trade_time) / self._interval)
            qty = int(qty_left / n)

            for i in range(n):

                if i == n-1:
                    # first child order
                    qty = qty_left

                child = ChildOrder(soid, i, trade_time, symbol, action, qty, endtime,
                                   ORDER_TYPE_MARKET)

                self._scheduler.push_order(trade_time, child)
                qty_left = qty_left - qty
                trade_time += self._interval
        return


    def pop_child_orders(self, timestamp):
        return self._scheduler.pop_orders(timestamp)