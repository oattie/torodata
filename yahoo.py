# load_yahoo_pdr.py @ 21:00 - 23:00
# get yesterday close, not today
# so, need to run another script to get current close and update CSV

# If something wrong with the download, try to upgrade
# pip install fix_yahoo_finance --upgrade --no-cache-dir

from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import datetime
from datetime import date
yf.pdr_override()

csv_dir = "../toroapp/static/data/"

symbol_file = open("set100.txt","r")
symbols = [x.strip('\n') for x in symbol_file.readlines()]

start = datetime.datetime(1990, 1, 1)
end = date.today()

i_stock = 0
for instrument in symbols:
    instrument = instrument.lower()
    i_stock = i_stock + 1
    print(i_stock, instrument)
    try:
        df = pdr.get_data_yahoo(instrument+'.BK', start=start, end=end)
        df.to_csv(csv_dir+instrument+".csv")
        print("Done")
        #print(csv_dir+instrument+".BK.csv")
    except:
        print("Retry...1")
        print(instrument)
        try:
            df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
            df.to_csv(csv_dir + instrument + ".BK.csv")
            print("Done")
        except:
            print("Retry...2")
            try:
                df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
                df.to_csv(csv_dir + instrument + ".BK.csv")
                print("Done")
            except:
                print("Retry...3")
                try:
                    df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
                    df.to_csv(csv_dir + instrument + ".BK.csv")
                    print("Done")
                except:
                    print("Retry...4")
                    try:
                        df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
                        df.to_csv(csv_dir + instrument + ".BK.csv")
                        print("Done")
                    except:
                        print("Retry...5")
                        try:
                            df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
                            df.to_csv(csv_dir + instrument + ".BK.csv")
                            print("Done")
                        except:
                            print("Retry...6")
                            try:
                                df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
                                df.to_csv(csv_dir + instrument + ".BK.csv")
                                print("Done")
                            except:
                                print("Retry...7")
                                try:
                                    df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
                                    df.to_csv(csv_dir + instrument + ".BK.csv")
                                    print("Done")
                                except:
                                    print("Retry...8")
                                    try:
                                        df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
                                        df.to_csv(csv_dir + instrument + ".BK.csv")
                                        print("Done")
                                    except:
                                        print("Retry...9")
                                        try:
                                            df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
                                            df.to_csv(csv_dir + instrument + ".BK.csv")
                                            print("Done")
                                        except:
                                            print("Retry...10")
                                            try:
                                                df = pdr.get_data_yahoo(instrument + '.BK', start=start, end=end)
                                                df.to_csv(csv_dir + instrument + ".BK.csv")
                                                print("Done")
                                            except:
                                                print("ERROR 10 re-tried Stop!")
