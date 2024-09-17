# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/backtest_loop.ipynb.

# %% auto 0
__all__ = ['backtest']

# %% ../nbs/backtest_loop.ipynb 4
import pandas as pd
import numpy as np
from parfor import parfor
from .data_interface import *

# %% ../nbs/backtest_loop.ipynb 5
def backtest(data,param):
    # Local variables
    start_date = param['start_date']
    er   = param['er_member_func']
    risk = param['risk_member_func']
    tc_func = param['tc_member_func']
    pm = param['pm_member_func']
    # Backtest time step: for now we trade at every step
    time_line = data.index.values # backtest frequency
    # Price time series assuming very specific yahoo format.
    model_prices = data.values # ohlcav
    if param['when_trade'] == 'open':
        trade_price = 0 
    else:
        trade_price = 4
    # Output storage array: create a 2D array
    position = []
    colnames = ['trade','position','er','vol','pnl0','pnl']
    items = [0 for _ in range(len(colnames))]
    # Backtest
    # (1) er+risk -> N
    # (2) pnl calculation with TC (fees and trading impact)
    t_loop = time_line#[:(start_date+100)]
    for tt in t_loop: # backtest loop
        if tt<time_line[start_date]:
            position.append(items)
            continue
        # Portfolio mananger: number of shares 
        t_data = model_prices[time_line<tt,:]
        t_yHat = er(t_data,param).y_hat()
        t_rHat = risk(t_data,param).risk_hat()
        t_p   = t_data[-1,4]
        t_pp  = t_data[-2,4]
        t_tp  = t_data[-1,trade_price]
        t_tpp = t_data[-2,trade_price]
        t_n_new = pm(t_data,param).allocation(t_yHat['y_hat'],t_rHat['vol_hat'],t_p)
    
        # Accountant: P&L
        n_t_minus1 = position[-2][1]
        n_t = position[-1][1]
        trade_t = n_t*t_tp # N(t)*trade_price(t)
        model_t = n_t*t_p # N(t)*model_price(t)
        trade_t_minus1 = n_t_minus1*t_tp
        model_t_minus1 = n_t_minus1*t_pp
        pnl0 = (model_t-trade_t)+(trade_t_minus1-model_t_minus1)
        tc0  = (n_t-n_t_minus1)
        tcc    = tc_func(t_data,param).TC(tc0)
        pnl = pnl0-tcc['TC']
        # Target position and trade 
        t_trade = t_n_new['N'] - n_t
        position.append([t_trade,t_n_new['N'],t_yHat['y_hat'],t_rHat['vol_hat'],float(pnl0),float(pnl)])
    
    return pd.DataFrame(position,index=time_line,columns=colnames)
