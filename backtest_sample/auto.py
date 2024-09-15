# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/data.yahoo.ipynb.

# %% auto 0
__all__ = ['yahoo']

# %% ../nbs/data.yahoo.ipynb 1
import yfinance as yf
import pandas as pd

# %% ../nbs/data.yahoo.ipynb 2
class yahoo:
    def __init__(self,ticker,start_date="1900-01-01"):
        self.ticker = ticker
        self.start_date = start_date
        self.data = None
    def _read_yahoo(self):
        """
        Reads data from Yahoo Finance.

        Args:
            ticker: The stock ticker symbol.
            start_date: The start date for the historical data.

        Returns:
            A pandas DataFrame containing the historical data.
        """
        try:
            self.data = yf.download(self.ticker, start=self.start_date)
        except Exception as e:
            print(f"Error reading data from Yahoo Finance: {e}")
    def _adj_yho(self):
        data = self.data    
        if data is not None:
            # Calculate adjustment factors
            data['adj_factor'] = data['Adj Close'] / data['Close']
            # Adjust open, high, and low prices
            data['Open'] = data['Open'] * data['adj_factor']
            data['High'] = data['High'] * data['adj_factor']
            data['Low'] = data['Low'] * data['adj_factor']
            data['Volume'] = data['Volume']/data['adj_factor'] # Vol increases if price decreases to keep V*P = cnst
            data['Volume'] = data['Volume'].apply(lambda z: int(z))
            # Remove the temporary 'adj_factor' column
            data = data.drop('adj_factor', axis=1)  
            # Keep original Close for future debug         
            return data
        else:
            return None

    def raw_data(self):
        self._read_yahoo()
        return self.data   
    def sim_data(self):
        if self.data is None:
            self._read_yahoo()
        return self._adj_yho()
        
