# We need to export data from SetSmart
# Open and save as TEXT tab file
import datetime
today = datetime.datetime.today().strftime('%Y%m%d')
#today = "20190109"

# THIS RUN WILL FIX IF CANNOT GET DATA ON SET, SETSMART IS DELAY FOR ONE DAY
# SO WE WILL USE, SET_OR_TH.PY INSTEAD

# Process write csv file
today_file_format = "set-history_EOD_"+datetime.datetime.today().strftime('%Y-%m-%d')
#today_file_format = "set-history_EOD_"+"2019-01-09"
myfile = "Setsmart_csv/"+today_file_format+".csv"
f = open(myfile, "w")
f.write('<TICKER>,<DTYYYYMMDD>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>\n')  

def parse_csv(myfilename="setsmart_file/setsmart.txt"):
    symbol_file = open(myfilename,"r")
    lines = [x.strip('\n') for x in symbol_file.readlines()]
    i = 0
    for line in lines:
        # ingore header
        if i<5:
            i = i+1
            continue
        values = line.split("\t")
        #Stop at the end
        if values[0] == "":
            break
        #print(values)
        # Extract Data
        values_ok = []
        for value in values:
            value = value.replace(",","")
            value = value.replace("\"","")
            values_ok.append(value)
        symbol = values_ok[1]
        # if symbol== "COM7":
        #     continue
        if symbol[-1] == ">":
            symbol = symbol.split(" ")
            symbol = symbol[0]
        open_p = float(values_ok[2])
        high_p = float(values_ok[2])
        low_p  = float(values_ok[2])
        close_p= float(values_ok[2])
        volume = float(values_ok[7])
        volume = int(volume)
        print([symbol,open_p,high_p,low_p,close_p,volume])
        f.write("%s,%s,%.2f,%.2f,%.2f,%.2f,%d\n" % (symbol,today,open_p,high_p,low_p,close_p,volume))

    symbol_file.close
parse_csv()
f.close()