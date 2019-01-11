import csv
import datetime
from bs4 import BeautifulSoup

today = datetime.datetime.today().strftime('%Y%m%d')
today_file_format = "set-history_EOD_"+datetime.datetime.today().strftime('%Y-%m-%d')

# Process write csv file
myfile = "set_or_th_csv/"+today_file_format+".csv"
outfile = open(myfile, "w")
outfile.write('<TICKER>,<DTYYYYMMDD>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>\n')  

with open(r'set_or_th_page/price.html', "r", encoding="utf8") as f:
    page = f.read()
soup = BeautifulSoup(page, "lxml")
for tr in soup.find_all('tr'):
    td = [td for td in tr.stripped_strings]
    if len(td) == 10:
        #print("================================================================Title")
        pass
    elif len(td) == 14:
        #print("================================================================Title")
        pass
    elif len(td) == 8: # SET INDEX INFO TABLE
        # Index, C, CHG, %CHG, High, Low, Vol, Val
        temp_td = []
        for item in td:
            if item == "-":
                item = 0
            if type(item) is str:
                item = item.replace(',','')
            temp_td.append(item)
        symbol = temp_td[0]
        close_p= float(temp_td[1])
        open_p= float(temp_td[1])   # Open = Close, Open price is not avai on set
        chg_p  = float(temp_td[2])
        pchg_p = float(temp_td[3])
        high_p = float(temp_td[4])
        low_p  = float(temp_td[5])
        vol    = int(temp_td[6])
        val    = float(temp_td[7])
        #print([symbol,close_p,chg_p,pchg_p,high_p,low_p,vol,val])
        outfile.write("%s,%s,%.2f,%.2f,%.2f,%.2f,%d\n" % (symbol,today,open_p,high_p,low_p,close_p,vol))
    elif len(td) == 11: # Normal table without Corporate event
    # Symbol, O, H, L, C, CHG, %CHG, Bid, Offer, Vol, Val
        temp_td = []
        for item in td:
            if item == "-":
                item = 0
            if type(item) is str:
                item = item.replace(',','')
            temp_td.append(item)
        symbol = temp_td[0]
        open_p = float(temp_td[1])
        high_p = float(temp_td[2])
        low_p  = float(temp_td[3])
        close_p= float(temp_td[4])
        chg_p  = float(temp_td[5])
        pchg_p = float(temp_td[6])
        bid_p  = float(temp_td[7])
        offer_p= float(temp_td[8])
        vol    = int(temp_td[9])
        val    = float(temp_td[10])
        #print([symbol,open_p,high_p,low_p,close_p,chg_p,pchg_p,bid_p,offer_p,vol,val])
        outfile.write("%s,%s,%.2f,%.2f,%.2f,%.2f,%d\n" % (symbol,today,open_p,high_p,low_p,close_p,vol))
    elif len(td) == 12: # Table with Corporate event
    # Symbol, Corp, O, H, L, C, CHG, %CHG, Bid, Offer, Vol, Val
        temp_td = []
        for item in td:
            if item == "-":
                item = 0
            if type(item) is str:
                item = item.replace(',','')                
            temp_td.append(item)
        symbol = temp_td[0]
        corp   = temp_td[1]
        open_p = float(temp_td[3])
        high_p = float(temp_td[3])
        low_p  = float(temp_td[4])
        close_p= float(temp_td[5])
        chg_p  = float(temp_td[6])
        pchg_p = float(temp_td[7])
        bid_p  = float(temp_td[8])
        offer_p= float(temp_td[9])
        vol    = int(temp_td[10])
        val    = float(temp_td[11])
        #print([symbol,corp,open_p,high_p,low_p,close_p,chg_p,pchg_p,bid_p,offer_p,vol,val])
        outfile.write("%s,%s,%.2f,%.2f,%.2f,%.2f,%d\n" % (symbol,today,open_p,high_p,low_p,close_p,vol))
    else:
        print("ERROR! Check Table")
outfile.close()