import pandas as pd
import pandas_datareader as web

data = pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')
data = data[1]

data = data[["Company","Symbol"]]
ticker_data = web.get_quote_yahoo(data["Symbol"])
ticker_data

ticker_data.columns
ticker_info = ticker_data[['epsForward','epsTrailingTwelveMonths','averageAnalystRating']].sort_values(by='epsForward', ascending=False)#FalseをTrueに変更すると小さい順に並ぶ
ticker_info