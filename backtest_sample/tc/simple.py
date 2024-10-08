# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/tc.simple.ipynb.

# %% auto 0
__all__ = ['simple']

# %% ../../nbs/tc.simple.ipynb 4
import pandas as pd
import numpy as np

# %% ../../nbs/tc.simple.ipynb 5
class simple:
    def __init__(self, data, param):
        """
        Initialize the simple class with data and parameters.
        
        Parameters:
        - data: A numpy array containing OHLCV (Open, High, Low, Close, Volume) data.
        - param: A dictionary containing parameters 'tc_slope' and 'tc_bias'.
        """
        self.ohlcv = data  # OHLCV data, assumes a specific format
        self.slope = param['tc_slope']  # Slope parameter for transaction cost calculation
        self.bias = param['tc_bias']    # Bias parameter for transaction cost calculation

    def TC(self, trade):
        """
        Calculate the transaction cost (TC) based on the given trade volume.
        
        Parameters:
        - trade: The trade volume.
        
        Returns:
        - A dictionary containing the calculated transaction cost.
        """
        V = self.ohlcv[:, 5]  # Extract the volume data from the OHLCV array
        p = self.ohlcv[:, 4]  # Extract the price data from the OHLCV array
        
        # The data is daily. Assume a 24-hour session.
        v = V / (24 * 60)  # Calculate the volume per minute
        vm = np.median(v[-40:])  # Calculate the median volume per minute over the last 40 periods
        dp = np.diff(p)  # Calculate the price differences
        ss = np.std(dp[-40:])  # Calculate the standard deviation of price differences over the last 40 periods
        
        out = {}
        # Calculate the transaction cost using the slope, standard deviation, trade volume, and bias
        out['TC'] = float(self.slope * (ss * np.abs(trade) / vm) + self.bias)
        
        return out

