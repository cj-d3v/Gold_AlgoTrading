class PositionManger(object):

    def __init__(self, config):
        self._data_provider = config.get_data_provider()
        pass

    def cal_daily_position(self):
        """
        Calculate the daily position.

        return: Dataframe with the follow fields:
            1. date
            2. symbol
            3. position
        """
        pass

    def cal_daily_return(self):
        pass

    def cal_max_drawdown(self):
        pass

    def cal_sharpe_ratio(self):
        pass