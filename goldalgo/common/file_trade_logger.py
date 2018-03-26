from goldalgo.common.trade_logger import *

class FileTradeLogger(TradeLogger):

    _name = 'File_Trade_Logger'

    def __init__(self):
        super().__init__()

    def log_project(self, project):
        pass

    def log_strategy_order(self, project, strategy_order):
        pass

    def log_child_order(self, project, child_order):
        pass

    def log_filled_order(self, project, filled_order):
        pass
