# global constant
ACTION_BUY = 'B'
ACTION_SELL = 'S'
MARKET_ORDER = 'M'
LIMIT_ORDER = 'L'

class StrategyOrder(object):

    def __init__(self, soid, portfolio, timestamp, symbol, action, qty, endtime, limitprice):

        self._soid = soid
        self._portfolio = portfolio
        self._timestamp = timestamp
        self._symbol = symbol
        self._action = action
        self._qty = qty
        self._endtime = endtime
        self._limitprice = limitprice

    def get_soid(self):
        return self._soid

    def get_portfolio(self):
        return self._portfolio

    def get_timestamp(self):
        return self._timestamp

    def get_symbol(self):
        return self._symbol

    def get_action(self):
        return self._action

    def get_qty(self):
        return self._qty

    def get_endtime(self):
        return self._endtime

    def get_limitprice(self):
        return self._limitprice


class ChildOrder(object):

    def __init__(self, coid, strategy_order, timestamp, symbol, action, qty, ordertype, limitprice):
        self._coid = coid
        self._strategy_order = strategy_order
        self._timestamp = timestamp
        self._symbol = symbol
        self._action = action
        self._qty = qty
        self._ordertype = ordertype
        self._limitprice = limitprice

    def get_coid(self):
        return self._coid

    def get_strategy_order(self):
        return self._strategy_order

    def get_timestamp(self):
        return self._timestamp

    def get_symbol(self):
        return self._symbol

    def get_action(self):
        return self._action

    def get_qty(self):
        return self._qty

    def get_ordertype(self):
        return self._ordertype

    def get_limitprice(self):
        return self._limitprice


class FilledOrder(object):

    def __init__(self, foid, child_order, timestamp, symbol, action, qty, price, market_impact):
        self._foid = foid
        self._child_order = child_order
        self._timestamp = timestamp
        self._symbol = symbol
        self._action = action
        self._qty = qty
        self._price = price
        self._market_impact = market_impact

    def get_foid(self):
        return self._foid

    def get_child_order(self):
        return self._child_order

    def get_timestamp(self):
        return self._timestamp

    def get_symbol(self):
        return self._symbol

    def get_action(self):
        return self._action

    def get_qty(self):
        return self._qty

    def get_price(self):
        return self._price

    def get_market_impact(self):
        return self._market_impact
