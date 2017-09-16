from datetime import datetime
from scrape_ticker_symbol import get_sp500_tickers
import csv

def write_tickers_to_file():

    sector_tickers = get_sp500_tickers()
    for sector in sector_tickers:
        filename = '{}-{}.csv'.format(sector, datetime.now().strftime('%Y-%m-%d'))
        tickers = sector_tickers.get(sector)
        with open (filename, 'wb') as f:
            wr = csv.writer(f, delimiter = ',')
            for ticker in tickers:
                # each ticker is an array of [symbol, location]
                wr.writerow(ticker)

if __name__ == '__main__':
    write_tickers_to_file()
