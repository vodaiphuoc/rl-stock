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

    stock_values['year'] = stock_values['time'].dt.year
    stock_values['month'] = stock_values['time'].dt.month
    stock_values['day'] = stock_values['time'].dt.day

    stock_values.drop_duplicates(inplace=True)
    stock_values.reset_index(drop = True, inplace = True)

    stock_values['time'] = pd.to_datetime(stock_values['time'], format="%Y-%m-%d")
    return stock_values



companies = [
    "AAV","CMG","VCB","ACB","TCB",
    "BID","FOC","FPT","HPG","GEX",
    "MSR","MVN","YEG","HSG","VHM",
    "MSN","VIC","PNJ","EIB","STB"
]

with pd.ExcelWriter('data/prices/all_prices.xlsx', engine='xlsxwriter') as writer:
    for symbol in companies:
        try:
            data = get_stock(stock_symbol= symbol, start_day="2010-01-01")
            data.to_excel(writer, sheet_name= symbol, index=False)
        except Exception as e:
            print(f'error {e} with symbol: {symbol}')
        