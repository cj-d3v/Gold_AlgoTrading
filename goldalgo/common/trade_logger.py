class TradeLogger():

    def get_name(self):
        return self._name

    def log_project(self, project):
        raise NotImplementedError()

    def log_strategy_order(self, project, strategy_order):
        raise NotImplementedError()

    def log_child_order(self, project, child_order):
        raise NotImplementedError()

    def log_filled_order(self, project, filled_order):
        raise NotImplementedError()
