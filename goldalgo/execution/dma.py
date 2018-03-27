class DMA(object):
    """
    Representation of the Direct Market Access. This can be pseudo, we will
    have an implementation for back-test, called Paper DMA.
    """

    def __init__(self):
        """
        Implementations should initiate their own states, e.g. a map for their
        pending limit orders.
        """
        pass

    def get_name(self):
        """
        Returns the name of an implementation. For debug or logging.
        """
        return self._name

    def execute_child_orders(self, config, timestamp, orders):
        """
        This method will be triggered by the main loop in a project, after
        children orders are popped out from the optimizer. Implementations
        should passed the orders to a direct market access API, or perform
        back-test with historical market data.

        config: you may access to the market data provider by this object.
        timestamp: the time point you assume where the back-test state is.
        orders: a list of children orders to be executed in DMA
        """
        raise NotImplementedError

    def pop_filled_order(self, timestamp):
        """
        Pop means retrieve elements and remove them from the stack. Given a
        time a point in back-test or live mode, pop the fulfilled order executed
        in direct market access (DMA).

        timestamp: the time point you assume where the back-test state is.

        returns: a list of fulfilled orders executed in DMA or an empty list.
        """
        raise NotImplementedError

