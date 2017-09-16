class Interval():
    # all available stock price changes at
    # interval [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    EACH_MIN = '1m'
    HOURLY = '1h'
    DAILY = '1d'
    FIVE_DAY = '5d'
    WEEKLY = '1wk'


class API_Url():
    crumb = ''
    historical_quotes = 'https://query1.finance.yahoo.com/v7/finance/download/'
    ticker_symbols = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'


class Stock_Data_Key():
    Time = 'time'
    High = 'high'
    Low = 'low'
    Open = 'open'
    Close = 'close'
    Adj_Close = 'adj_close'
    Volume = 'volume'

class Kernal():
    Gaussian = 'gaussian'
    Tophat =  'tophat'
    Epanechnikov = 'epanechnikov'


DATE_PATTERN = '%Y-%m-%d'


Stock_Val_Keys = [Stock_Data_Key.High, Stock_Data_Key.Low, Stock_Data_Key.Open, Stock_Data_Key.Close, Stock_Data_Key.Adj_Close, Stock_Data_Key.Volume]
