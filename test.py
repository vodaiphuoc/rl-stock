from datetime import datetime
from vnstock import Vnstock
stock = Vnstock().stock(symbol='VNINDEX', source='VCI')


start_day="2010-01-01"
print(stock.quote.history(
    start = start_day, 
    end = str(datetime.now().date()),
    interval = '1D')
)

# list_symbols = stock.listing.symbols_by_exchange()



# companies = [
#     "VTP","CMG","VCB","ACB","TCB",
#     "BID","TCL","FPT","HPG","GEX",
#     "TRA","VRC","YEG","HSG","VHM",
#     "MSN","VIC","PNJ","EIB","STB"
# ]

# # MVN, MSR, FOC, AVV

# df = list_symbols[['symbol','exchange']]
# res = df[df.symbol.isin(companies)]
# print(res)