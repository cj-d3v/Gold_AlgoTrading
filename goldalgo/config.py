from strategy.porfolio_a import *
from strategy.porfolio_b import *
from execution.twap import *
from execution.vwap import *
from execution.paper_dma import *
from common.file_trade_logger import *

STRATEGY_PORT_A = 11
STRATEGY_PORT_B = 12
OPTIMIZER_TWAP = 21
OPTIMIZER_VWAP = 22
DMA_PAPER = 31
#DMA_IB = 32
DATA_PROVIDER_FILE = 41
#DATA_PROVIDER_IB = 42
TRADE_LOGGER_FILE = 51
#TRADE_LOGGER_MYSQL = 52

class Config(object):

    def __init__(self):
        self._start_date = None
        self._end_date = None
        self._strategy_type = None
        self._optimizer_type = None
        self._dma_type = None
        self._data_provider_type = None
        self._logger_type = None

        self._strategy = None
        self._optimizer = None
        self._dma = None
        self._data_provider = None
        self._logger = None

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def set_strategy(self, type):
        if self._strategy is not None:
            assert False
        self._strategy_type = type

    def set_optimizer(self, type):
        if self._optimizer is not None:
            assert False
        self._optimizer_type = type

    def set_dma(self, type):
        if self._dma is not None:
            assert False
        self._dma_type = type

    def set_data_provider(self, type):
        if self._data_provider is not None:
            assert False
        self._data_provider_type = type

    def set_logger(self, type):
        if self._logger is not None:
            assert False
        self._logger_type = type

    def get_strategy(self):
        if self._strategy is not None:
            return self._strategy
        if self._strategy_type == STRATEGY_PORT_A:
            return PFA_Strategy()
        elif self._strategy_type == STRATEGY_PORT_B:
            return PFB_Strategy()
        raise ValueError()

    def get_optimizer(self):
        if self._optimizer is not None:
            return self._optimizer
        if self._optimizer_type == OPTIMIZER_TWAP:
            return TWAP()
        elif self._optimizer_type == OPTIMIZER_VWAP:
            return VWAP()
        raise ValueError()

    def get_dma(self):
        if self._dma is not None:
            return self._dma
        if self._dma_type == DMA_PAPER:
            return PaperDMA()
        raise ValueError()

    def get_data_provider(self):
        if self._data_provider is not None:
            return self._data_provider
        if self._data_provider_type == DATA_PROVIDER_FILE:
            #return FileDataProvider()
            pass
        raise ValueError()

    def get_logger(self):
        if self._logger is not None:
            return self._logger
        if self._logger_type == TRADE_LOGGER_FILE:
            return FileTradeLogger()
        raise ValueError()
