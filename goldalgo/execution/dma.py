class DMA(object):

    def __init__(self):
        self._child_orders = []

    def execute_child_orders(self, timestamp, orders):
        raise NotImplementedError

    def get_filled_order(self, timestamp):
        raise NotImplementedError

