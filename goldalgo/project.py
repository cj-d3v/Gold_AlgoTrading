from goldalgo.strategy.porfolio_a import *
from goldalgo.strategy.porfolio_b import *
from goldalgo.execution.twap import *
from goldalgo.execution.vwap import *
from goldalgo.execution.paper_dma import *
#from goldalgo.common import *

class Project(object):

    # static variables
    _strategy_list = ['Portfolio_A', 'Porfolio_B', 'Portfolio_C']
    _optimizer_list = ['TWAP', 'VWAP']
    _dma_list = ['Paper_DMA']

    def __init__(self):
        pass

    def set_strategy_name(self, name):
        assert (name in self._strategy_list)
        self.strategy_name = name

    def set_optimizer_name(self, name):
        assert (name in self._optimizer_list)
        self.optimizer_name = name

    def set_dma_name(self, name):
        assert (name in self._dma_list)
        self.dma_name = name

    def get_strategy(self):
        if (self.strategy_name == self._strategy_list[0]):
            return PFA_Strategy()
        elif (self.strategy_name == self._strategy_list[0]):
            return PFB_Strategy()
        raise ValueError

    def get_optimizer(self):
        if (self.optimizer_name == self._optimizer_list[0]):
            return TWAP()
        elif (self.optimizer_name == self._optimizer_list[1]):
            return VWAP()
        raise ValueError
    
    def get_dma(self):
        return PaperDMA()

    def run(self):
        strategy = self.get_strategy()
        optimizer = self.get_optimizer()
        dma = self.get_dma()

        timestamp = 0
        # for each discrete timestamp
        sorders = strategy.generate_orders(timestamp)
        #logger.log_strategy_orders(sorders)
        if len(sorders) > 0:
            optimizer.push_strategy_orders(timestamp, sorders)

        corders = optimizer.pop_child_orders(timestamp)
        #logger.log_child_orders(corders)
        if len(corders) > 0:
            dma.execute_child_orders(timestamp, corders)

        forders = dma.pop_filled_order(timestamp)
        #logger.log_filled_orders(forders)
