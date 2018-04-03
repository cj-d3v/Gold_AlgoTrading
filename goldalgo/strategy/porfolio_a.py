from strategy.template import *
from strategy.vol_imp import *

class PFA_Strategy(Strategy):
    
    _name = 'Portfolio_A'
    
    def __init__(self):
        super().__init__()
        # init your own states
        self._timedelta=15 #generate predict signal each 15 minutes
        self._opt_qty=None
        self._gold_qty=None


    def get_data(self,config,now_time):
        # expect data format:
        # 1) type: DataFrame
        # 2) time-scope: from start date to end date
        # 3) include call and put data with "Type,S0,K,t,T,r,q,V", in which q=0 in default
        options_data=config.get_data_provider().gold_options(startdate=config.get_start_date(),enddate=config.get_end_date(),expriy_nearest=5)
        # should fullfill data_provider().gold_options()
        spot_gold_data=config.get_data_provider().gold_spot_price(startdate=config.get_start_date(),enddate=config.get_end_date())
        # should fullfill data_provider().gold_spot_price()
        call_short_data=options_data.last(time=now_time,type='call')
        put_short_data=options_data.last(time=now_time,type='put')
        spotprice_gold=spot_gold_data.last(time=now_time)
        return call_short_data,put_short_data,spotprice_gold

    def term_structure(self,config,now_time):
        # this function returns with a 2-dimension array:
        # 1) the implied volatility of call, witn 5 nearest expriy dates
        # 2) the implied volatility of put, with 5 nearest expriy dates
        data=self.get_data(config,now_time)
        c_data=data[0] # strike price,expiry date, last price,with 5 records
        p_data=data[1] # strike price,expiry date, last price,with 5 records
        S0=data[2]
        t=0
        q=0
        r=config.get_data_provider.get_interest_rate(startdate=config.get_start_date(),enddate=config.get_end_date())
        # should fullfill data_provider().get_interest_rate()
        c_impvol=[]
        p_impvol=[]
        for i in range(5):
            T=c_data[i][1]-now_time # need to be further adjusted
            imv=imp_vol('call',S0,c_data[i][0],t,T,r,q,c_data[i][2])
            c_impvol.append(imv)
        for i in range(5):
            T=c_data[i][1]-now_time # need to be further adjusted
            imv=imp_vol('put',S0,p_data[i][0],t,T,r,q,c_data[i][2])
            p_impvol.append(imv)
        return np.array(c_impvol),np.array(p_impvol)

    def generate_orders(self, config, timestamp):
        now_time=timestamp  # need to be further adjusted to get current time
        c_impvol,p_impvol=self.term_structure(config,now_time)
        dft_T=(c_impvol-p_impvol).mean()
        dft_t=(c_impvol-p_impvol)[0]
        trade_order=[]
        opt_qty=self._opt_qty
        gold_qty=self._gold_qty
        if dft_t-dft_T>=0:
            # the price of gold will go down, long put and short call after hedging positions
            trade_order=['heging','long put','short call','sell gold']
        elif  dft_t-dft_T<=0:
            # the price of gold will go up, long call and short put after hedging positions
            trade_order=['heging','long call','short put','buy gold']
        return trade_order,opt_qty,gold_qty