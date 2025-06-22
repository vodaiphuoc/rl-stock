from vnstock3 import Listing


listing = Listing()
symbols = listing.all_symbols()


symbols.to_excel("data/symbols/all_symbols.xlsx")