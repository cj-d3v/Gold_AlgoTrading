class TradeScheduler(object):
    """
    This is a helper class for statically schedule-driver execution algorithm,
    like TWAP, VWAP, etc. where the trading trajectory is planning beforehand.
    """

    def __init__(self):
        self._schedules = []
        self._orders = []

    def push_order(self, timestamp, order):
        """
        Add a chile order together with its planned execution time.

        timestamp: the current or a future execution time.
        order: a child order to be executed
        """
        self._schedules.append(timestamp)
        self._orders.append(order)

    def pop_orders(self, timestamp):
        """
        Retrieve and remove a list of executable child orders, given the
        current timestamp.

        timestamp: the current timestamp.

        returns: a list of executable child orders, or just an empty list
        """
        indices = [i for i, t in sorted(enumerate(self._schedules), reverse=True) if t <= timestamp]
        [self._schedules.pop(i) for i in indices]
        orders = [self._orders.pop(i) for i in indices]
        return orders
