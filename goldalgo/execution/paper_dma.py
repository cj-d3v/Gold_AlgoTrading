from goldalgo.execution.dma import *

class PaperDMA(DMA):

    _name = 'Paper_DMA'

    def execute_child_orders(self, config, timestamp, orders):
        pass

    def pop_filled_order(self, timestamp):
        return []
