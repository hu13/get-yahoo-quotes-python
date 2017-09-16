#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup
from constants import API_Url

def _scrape_list(site):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)

    table = soup.find('table', {'class': 'wikitable sortable'})
    sector_tickers = dict()
    for row in table.findAll('tr'):
        col = row.findAll('td')

        if len(col) > 0:
            sector = str(col[3].string.strip()).lower().replace(' ', '_')
            ticker = str(col[0].string.strip())
            location = ''
            if (len(col) - 3) > 0:
                location = str(col[len(col)-3].string).strip()

            if sector not in sector_tickers:
                sector_tickers[sector] = list()
            sector_tickers[sector].append([ticker, location])
    return sector_tickers

def get_sp500_tickers():
    return _scrape_list(API_Url.ticker_symbols)
