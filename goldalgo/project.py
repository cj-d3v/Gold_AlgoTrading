from goldalgo.config import *

class Project(object):

    def __init__(self, start_date, end_date, heartbeat, config):
        self.config = config
        self.start_date = start_date
        self.end_date = end_date
        self.heartbeat = heartbeat

    def run(self):
        strategy = self.config.get_strategy()
        optimizer = self.config.get_optimizer()
        dma = self.config.get_dma()
        logger = self.config.get_logger()
        logger.log_project(self)

        timestamp = 0

        # for each discrete timestamp
        sorders = strategy.generate_orders(self.config, timestamp)
        if len(sorders) > 0:
            logger.log_strategy_orders(self, sorders)
            optimizer.execute_strategy_orders(self.config, timestamp, sorders)

        corders = optimizer.pop_child_orders(timestamp)
        if len(corders) > 0:
            logger.log_child_orders(self, corders)
            dma.execute_child_orders(self.config, timestamp, corders)

        forders = dma.pop_filled_order(timestamp)
        if len(forders) > 0:
            logger.log_filled_orders(self, forders)
        #

        print('completed.')
