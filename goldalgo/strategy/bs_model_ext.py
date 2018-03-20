# Black_Scholes_Model_Extended
# Author: Wu Kangzhang
# Institution: HKU
# Date: March_2018

import numpy as np
from scipy.stats import norm

class bs(object):
    def __init__(self, future_type, asset_price, strike_price, current_time, mature_time, vol, rate,repo_q):
        if str.upper(future_type) == 'CALL' or str.upper(future_type) == 'PUT':
            self.type = future_type
            self.S = asset_price
            self.K = strike_price
            self.t = current_time
            self.T = mature_time
            self.vol = vol
            self.r = rate
            self.q = repo_q
            self.val = np.dtype(np.float32)
        else:
            print("Type of future is invalid.\nPlease input with \'call\' or \'put\'.")

    def d1_d2(self):
        d1 = (np.log(self.S/self.K)+(self.r-self.q)*(self.T-self.t))/(self.vol*np.sqrt(self.T-self.t)) \
            + 0.5*self.vol*np.sqrt(self.T-self.t)
        d2 = (np.log(self.S/self.K)+(self.r-self.q)*(self.T-self.t))/(self.vol*np.sqrt(self.T-self.t)) \
            - 0.5*self.vol*np.sqrt(self.T-self.t)
        return d1, d2

    def value(self):
        d1,d2 = self.d1_d2()
        if str.upper(self.type) == 'CALL':
            self.val = self.S*np.exp(self.q*(self.t-self.T))*norm.cdf(d1) \
                       - self.K*np.exp(self.r*(self.t-self.T))*norm.cdf(d2)
        elif str.upper(self.type) == 'PUT':
            self.val = self.K*np.exp(self.r*(self.t-self.T))*norm.cdf(-d2) \
                       - self.S*np.exp(self.q*(self.t-self.T))*norm.cdf(-d1)
        return self.val
