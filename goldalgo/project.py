import datetime
from goldalgo.config import *

MINUTES = 11
HOURS = 12
DAYS = 13

class Project(object):

    _date_format = '%Y-%m-%d'

    def __init__(self, start_date, end_date, heartbeat, unit, config):
        self.config = config

        self.start_date = datetime.datetime.strptime(start_date, self._date_format)
        self.end_date = datetime.datetime.strptime(end_date, self._date_format)
        if (self.start_date > self.end_date):
            raise ValueError()

        if (unit == MINUTES):
            self.heartbeat = datetime.timedelta(minutes=heartbeat)
        elif (unit == HOURS):
            self.heartbeat= datetime.timedelta(hours=heartbeat)
        elif (unit == DAYS):
            self.heartbeat = datetime.timedelta(days=heartbeat)
        else:
            raise ValueError()


    def run(self):
        strategy = self.config.get_strategy()
        optimizer = self.config.get_optimizer()
        dma = self.config.get_dma()
        logger = self.config.get_logger()
        logger.log_project(self)

        timestamp = self.start_date

        while (timestamp <= self.end_date):

            print('timestamp=', timestamp)

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

            timestamp = timestamp + self.heartbeat

        print('completed.')
