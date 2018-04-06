from goldalgo.config import *
import datetime

class Project(object):

    def __init__(self, config):
        self._config = config

    def run(self):
        strategy = self._config.get_strategy()
        optimizer = self._config.get_optimizer()
        dma = self._config.get_dma()
        logger = self._config.get_logger()
        logger.log_project(self)

        timestamp = self._config.get_start_date()

        while (timestamp <= self._config.get_end_date()):

            print('timestamp=', timestamp)

            sorders = strategy.generate_orders(self._config, timestamp)
            if len(sorders) > 0:
                logger.log_strategy_orders(self, sorders)
                optimizer.execute_strategy_orders(self._config, timestamp, sorders)

            corders = optimizer.pop_child_orders(timestamp)
            if len(corders) > 0:
                logger.log_child_orders(self, corders)
                dma.execute_child_orders(self._config, timestamp, corders)

            forders = dma.pop_filled_order(timestamp)
            if len(forders) > 0:
                logger.log_filled_orders(self, forders)

            timestamp = timestamp + self._config.get_heartbeat()

        print('completed.')
