class Optimizer(object):

    def __init__(self):
        pass

    def get_name(self):
        return self._name

    def add_strategy_orders(self, timestamp, orders):
        raise NotImplementedError

    def get_child_orders(self, timestamp):
        raise NotImplementedError
