from goldalgo.common.data_provider import *
from goldalgo.common.file_symbol import *

class FileDataProvider(DataProvider):

    def __init__(self, config):
        pass

    def list_contract_maturities(self, asset_code, timestamp):
        pass

    def list_option_strikes(self, asset_code, maturity, type):
        pass

    def get_index(self, config, asset_code):
        s = FileSymbol(config, 'GC')
        return s

    def get_future(self, config, asset_code, maturity):
        s = FileSymbol(config, 'GCK18')
        return s

    def get_option(self, config, asset_code, maturity, strike, type):
        s = FileSymbol(config, 'OGK181300P')
        return s

    def get_risk_free_interest(self, date, maturity):
        pass


