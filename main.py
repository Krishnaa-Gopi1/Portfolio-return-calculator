import yfinance as yf
import pandas as pd 


tickers = ['AAPL','TSLA','MSFT']

import yfinance as yf

tickers = ['AAPL', 'MSFT', 'TSLA']
data = yf.download(tickers, start='2025-05-01', end='2025-05-27')

# Save Close prices only
data['Close'].to_csv('close_prices.csv')

# Save Open prices only
data['Open'].to_csv('open_prices.csv')

# Save Volume only
data['Volume'].to_csv('volume.csv')



close_df = pd.read_csv('close_prices.csv', index_col=0, parse_dates=True)
open_df = pd.read_csv('open_prices.csv', index_col=0, parse_dates=True)
volume_df = pd.read_csv('volume.csv', index_col=0, parse_dates=True)

print(close_df)