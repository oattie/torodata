import pandas as pd
import numpy as np

symbol_file = open("today_trade_symbol.txt","r")
symbols = [x.strip('\n') for x in symbol_file.readlines()]

for symbol in symbols:
    print("Start generating JSON..."+symbol)
    pd_data = pd.read_csv("../toroapp/static/data/"+symbol.lower()+".csv")
    pd_data['Date'] = pd.DatetimeIndex ( pd_data['Date'] ).astype ( np.int64 )/1000000
    pd_data.Date = pd_data.Date.astype(np.int64)
    #print(pd_data.dtypes)
    json_data = pd_data.to_json("../toroapp/static/json/"+symbol.lower()+".json", orient="values")