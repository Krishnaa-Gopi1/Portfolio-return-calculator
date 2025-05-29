import yfinance as yf
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


ticker_input = input("Enter stock tickers seperated by commas : ")
tickers = ticker_input.split(',')
tickers = [ticker.strip() for ticker in tickers]

while(True):
    weights_input = input("Enter weights of tickers seperated by commas: ")
    weights = list(map(float,weights_input.split(',')))
    if abs(sum(weights) - 1.0) < 1e-6 and len(weights)==len(tickers):
        break
    print("Sum of weights is not 1. Try again.")



data = yf.download(tickers, start='2025-05-01', end='2025-05-27')
# save Close prices 
data['Close'].to_csv('close_prices.csv')




close_df = pd.read_csv('close_prices.csv', index_col=0, parse_dates=True)


returns = close_df.pct_change().dropna()  #gives daily percentage returns




portfolio_returns = returns.dot(weights)   #daily returns  of portfolio as time series

annual_return = portfolio_returns.mean() * 252 #annual returns for 252 days of trade
print("Annual Return in percentage : " , annual_return)

annual_volatility = portfolio_returns.std() * np.sqrt(252) # .std() returns standard deviation of daily returns and multiplying it with sq root of time gives annual volatility
print("Annual volatility : " , annual_volatility)

risk_free_rate = 0
sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility
print("Sharpe ratio considering risk free rate is 0 : " , sharpe_ratio)

cumulative_returns = (1 + portfolio_returns).cumprod()
cumulative_returns.plot(title="Portfolio returns over time")
plt.xlabel('Date')
plt.ylabel('Cumulative return')
plt.show()