# Calculate implied volatility based on Black_Scholes_Model_Extended
# Author: Wu Kangzhang
# Institution: HKU
# Date: March_2018

import numpy as np
from scipy.stats import norm
import BS_MODEL_EXT as bsm

def imp_vol(Type,S0,K,t,T,r,q,V,tol=1e-8,sigmadiff=1,iter_num=200):
    sigma=np.sqrt(2*abs((np.log(S0/K)+(r-q)*(T-t))/(T-t)))
    n=1
    # print('Iteration '+str(n)+':sigma='+str(sigma)+'\n')
    if str.upper(Type)=='CALL':
        while sigmadiff>=tol and n<iter_num:
            c_bs=bsm.bs('CALL',S0,K,t,T,sigma,r,q)
            c=c_bs.value()
            d1=c_bs.d1_d2()[0]
            c_vega=S0*np.exp(q*(t-T))*np.sqrt(T-t)*norm.pdf(d1)
            increment=(c-V)/c_vega
            sigma=sigma-increment
            n=n+1
            # print('Iteration '+str(n)+':sigma='+str(sigma)+'\n')
            sigmadiff=abs(increment)
    elif str.upper(Type)=='PUT':
        while sigmadiff>=tol and n<iter_num:
            p_bs=bsm.bs('PUT',S0,K,t,T,sigma,r,q)
            p=p_bs.value()
            d1=p_bs.d1_d2()[0]
            p_vega=S0*np.exp(q*(t-T))*np.sqrt(T-t)*norm.pdf(d1)
            increment=(p-V)/p_vega
            sigma=sigma-increment
            n=n+1
            # print('Iteration '+str(n)+':sigma='+str(sigma)+'\n')
            sigmadiff=abs(increment)
    return sigma
