import numpy as np
import datetime as dt

class Strategy(object):

    def __init__(self):
        pending_orders = {} # map {start_time: orders}

    def get_name(self):
        return self._name

    def _new_order_id(self):
        suffix = str(np.random.randint(0, 100))
        date_str = str(dt.datetime.now().strftime("%Y%m%d%H%M"))
        return 'SO' + date_str + suffix

    def generate_orders(self, timestamp):
        raise NotImplementedError