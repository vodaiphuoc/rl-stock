'''
from vnstock3 import Listing


listing = Listing()
symbols = listing.all_symbols()


symbols.to_excel("data/symbols/all_symbols.xlsx")
'''


import json
import glob
from typing import Literal, List, Dict, Union
from datetime import datetime
import re
from collections import defaultdict
from vnstock import Vnstock
import os
import pandas as pd
import numpy as np


def get_stock(stock_symbol: str, start_day:str = "2010-01-01")->pd.DataFrame:
    acb_stocks = Vnstock().stock(symbol=stock_symbol, source= "VCI")
    stock_values =  acb_stocks.quote.history(
        start = start_day, 
        end = str(datetime.now().date()),
        interval = '1D'
    )
    stock_values = stock_values.sort_values(by = 'time')
    print(stock_symbol, stock_values['time'].head(5))

    stock_values['year'] = stock_values['time'].dt.year
    stock_values['month'] = stock_values['time'].dt.month
    stock_values['day'] = stock_values['time'].dt.day

    stock_values.drop_duplicates(inplace=True)
    stock_values.reset_index(drop = True, inplace = True)

    stock_values['date'] = stock_values['time']

    stock_values['stock'] = stock_symbol
    return stock_values

companies = [
    "VTP","CMG","VCB","ACB","TCB",
    "BID","TCL","FPT","HPG","GEX",
    "TRA","VRC","YEG","HSG","VHM",
    "MSN","VIC","PNJ","EIB","STB"
]

start_day="2018-11-26"
df_list = [get_stock(stock_symbol= symbol, start_day=start_day) 
           for symbol in companies
]
total_df = pd.concat(df_list)
total_df.to_excel('data/prices/all_prices.xlsx',index=False)

# get market data
market_stock = Vnstock().stock(symbol='VNINDEX', source='VCI')
market_data = market_stock.quote.history(
    start = start_day, 
    end = str(datetime.now().date()),
    interval = '1D')

market_data['date'] = market_data['time']
market_data.to_excel('data/prices/vnindex.xlsx',index=False)
