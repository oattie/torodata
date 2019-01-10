# This file read a html file form SET, AOM page
# Need to save the file locally before parsing
import csv
import datetime
from lxml import html

with open(r'set_or_th_page/price.html', "r", encoding="utf8") as f:
    page = f.read()

# AGRI & INDS: AGRI = 2
# AGRI & INDS: FOOD = 3
# CONSUMER: FASION  = 4
# CONSUMER: OFFICE  = 5
# CONSUMER: MED     = 6
# FINANCIAL:  BANK  = 7
# FINANCIAL:  SEC   = 8
# FINANCIAL: INSURE = 9
# INDUS: CAR        = 10
# INDUS: MACHINE    = 11
# INDUS: PAPER      = 12
# INDUS: CHEM       = 13
# INDUS: PKG        = 14
# INDUS: METAL      = 15
# REALESTATE:CONMAT = 16
# REALESTATE:PROP   = 17
# REALESTATE:TRUST  = 18
# REALESTATE:CONST  = 19
# ENERGY: POWER     = 20
# RESOURCE: MINING  = 21
# Service: RETAIL   = 22
# SERVICE: MED      = 23
# SERVICE: ADS      = 24
# SERVICE: NICHE    = 25
# SERVICE: TRAVEL   = 26
# SERVICE: LOGIS    = 27
# TECH: ELEC        = 28
# TECH: COMM        = 29
# STOCK: -F         = 30
# STOCK: -P         = 31
# WORRANT: -W       = 32
# DW                = 33
# ETF               = 34
# DR                = 35
# TRUST             = 36

today = datetime.datetime.today().strftime('%Y%m%d')
# Process write csv file
myfile = "set_or_th_csv/"+today+".csv"
f = open(myfile, "a")
f.write('<TICKER>,<DTYYYYMMDD>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>\n')  

# As of 10 Jan 2019 = 36 Tables
# Get list of symbols in each table
# Each Table: /div/div[2]/div/div/div/div[x]/table
i=2
while i<36:              
    tree = html.fromstring(page)
    symbols = tree.xpath('//*[@id="maincontent"]/div/div[2]/div/div/div/div['+str(i)+']/table/tbody/tr/td/a/text()')
    symbols_ok = []
    for symbol in symbols:
        symbols_ok.append(symbol.strip())
    #print(symbols_ok)

    j = 1
    for symbol_ok in symbols_ok:
        if symbol_ok == "COM7":
            continue
        print(symbol_ok)
        # Get Open, High, Low, Close, Bid, Offer, Vol, Val
        # Each Row identify by /tr[x]/td/text()
        ohlcvs = tree.xpath('//*[@id="maincontent"]/div/div[2]/div/div/div/div[2]/table/tbody/tr['+str(j)+']/td/text()')
        ohlcvs_ok = []
        for ohlcv in ohlcvs:
            ohlcv = ohlcv.strip()
            if ohlcv =='':
                continue
            ohlcv = ohlcv.replace('+',"0")
            ohlcv = ohlcv.replace('-',"0")
            ohlcv = ohlcv.replace(',',"")
            ohlcv = float(ohlcv)
            ohlcv = round(ohlcv, 2)
            ohlcvs_ok.append(ohlcv)
        # This handle '-' non-change case
        if ohlcvs == []:
            ohlcvs_ok.append(0)    # Open
            ohlcvs_ok.append(0)    # High
            ohlcvs_ok.append(0)    # Low
            ohlcvs_ok.append(0)    # Close
            ohlcvs_ok.append(0)    # Vol
            ohlcvs_ok.append(0)    # Val
        print(ohlcvs_ok)

        # Get Change, and % Change
        # Each Row identify by /tr[x]/td/text()
        chgs = tree.xpath('//*[@id="maincontent"]/div/div[2]/div/div/div/div[2]/table/tbody/tr['+str(j)+']/td/font/text()')
        chgs_ok = []
        for chg in chgs:
            chg = float(chg)
            chg = round(chg, 2)
            chgs_ok.append(chg)
        # This handle '-' non-change
        if chgs == []: 
            chgs_ok.append(0)   # Change
            chgs_ok.append(0)   # % Change
        print(chgs_ok)
        j = j+1 # loop all lines in the tables
        f.write("%s,%s,%.2f,%.2f,%.2f,%.2f,%d,%d\n" % (symbol_ok,today,ohlcvs_ok[0],ohlcvs_ok[1],ohlcvs_ok[2],ohlcvs_ok[3],ohlcvs_ok[4],ohlcvs_ok[5]))
    i = i+1     # loop all tables
f.close()
