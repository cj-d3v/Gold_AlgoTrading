import pandas as pd
from goldalgo.common.symbol import *

class FileSymbol(Symbol):

    def __init__(self, config, symbol_code):
        start_date = config.get_start_date()
        end_date = config.get_end_date()
        # load symbol data into memory

    def get_hist_data(self, start_datetime, end_datetime, bar_size, fields):
        df = pd.Dataframe()
        return df

