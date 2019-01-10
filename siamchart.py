# Because Yahoo cannot provide real-time CSV for latest OHLC
# This script will download data from SiamChart.com
# Then, update all CSV files

#from selenium import webdriver
from datetime import date
import os
import time
import subprocess
import csv
import datetime
today = datetime.datetime.today().strftime('%Y-%m-%d')

def download_siamchart():
    # Uncomment 3 lines below for LINUX
    #from pyvirtualdisplay import Display
    #display = Display(visible=0, size=(1024, 768))
    #display.start()
    driver = webdriver.Chrome(executable_path='/home/quant/toroapp/libcode/chromedriver')
    driver.implicitly_wait(30)
    #driver.maximize_window()
    driver.get("https://www.siamchart.com")
    user_name_field = driver.find_element_by_name("vb_login_username")
    user_name_field.clear()
    user_name_field.send_keys("toromagn")
    password_field = driver.find_element_by_name("vb_login_password")
    password_field.clear()
    password_field.send_keys("Fpus83#*")
    login_button = driver.find_element_by_id("search-submit")
    login_button.click()
    time.sleep(3)
    driver.get("http://siamchart.com/stock/")
    daily_download_link = driver.find_element_by_xpath("//*[@id=\"toptable\"]/div[3]/table/tbody/tr[4]/td[2]/a")
    daily_download_link.click()
    time.sleep(3)


def unzipfile():
    subprocess.call('unzip /home/quant/Downloads/set-archive_EOD_LAST.zip -d /home/quant/Downloads/setdata',shell=True)
    subprocess.call('mv /home/quant/Downloads/setdata/D\:/SET-ARCHIVE/EOD/*.csv data.csv',shell=True)
    subprocess.call('rm -rf /home/quant/Downloads/setdata',shell=True)


def parse_symbols(myfilename="data.csv"):
    # This function read daily file from siamchart to extact all symbols traded.
    symbol_file = open(myfilename,"r")
    all_sym_file = open("today_trade_symbol.txt", "w")
    lines = [x.strip('\n') for x in symbol_file.readlines()]
    i = 0
    for line in lines:
        if i==0:
            i = i+1
            continue
        values = line.split(",")
        symbol = values[0]
        all_sym_file.writelines("%s\n" % symbol)
        i = i+1
    symbol_file.close
    all_sym_file.close

def read_historical_csv_update_data_folder(source_data_dir):
    csv_dir = "data/"
    # all files .csv in ./data1970to2018 folder
    all_files = os.listdir(source_data_dir)
    all_files = sorted(all_files)

    for myfile in all_files:
        print("process..."+myfile)
        parse_symbols(source_data_dir+myfile)
        symbol_file = open("today_trade_symbol.txt","r")
        symbols = [x.strip('\n') for x in symbol_file.readlines()]
        
        with open(source_data_dir+myfile) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            num_row = 0
            for row in readCSV:
                if num_row == 0:
                    header = row
                    num_row = num_row+1
                else:
                    symbol = row[0]
                    # Process Year-Month-Date format
                    year = row[1][:4]
                    month = row[1][4:-2]
                    day = row[1][-2:]
                    date = year + '-' + month + '-' + day
                    open_price = row[2]
                    high_price = row[3]
                    low_price = row[4]
                    close_price = row[5]
                    volume = row[6]
                    adj_close = close_price
                    #print(symbol)

                    # Process write csv file
                    file_exists = os.path.isfile(csv_dir + symbol.lower() + ".csv")
                    if symbol in symbols:
                        with open(csv_dir + symbol.lower() + ".csv", 'a') as csvfile:
                            headers=['Date','Open','High','Low','Close','Adj Close', 'Volume']
                            writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
                            if not file_exists:
                                writer.writeheader()    
                            writer.writerow({'Date': date, 'Open': open_price, 'High': high_price, 'Low': low_price, 'Close': close_price, 'Adj Close': adj_close, 'Volume': volume})
                    num_row = num_row+1


if __name__ == "__main__":
    # FOLDER PROCESSING #
    # Run only once to initialize the data from 1970 to 2018
    # Process write csv file
    #today = "2019-10-10"
    file_exists = os.path.isfile("data/set.csv")
    if not file_exists:
        read_historical_csv_update_data_folder("data1970to2018/")
        read_historical_csv_update_data_folder("data2019/")
        read_historical_csv_update_data_folder("Setsmart_csv/")
        read_historical_csv_update_data_folder("set_or_th_csv/")
    else:
        # Check if the file already has the data for today
        # Before writing!
        with open("set.csv", 'r') as checkfile:
            last_line = checkfile.readlines()[-1]
            filedate = last_line.split(",")
            if filedate[0] == today:
                exit()
            else:
                # EVERYDAY - UPDATE HERE
                #read_historical_csv_update_data_folder("Setsmart_csv/")
                read_historical_csv_update_data_folder("set_or_th_csv/")

    #unzipfile()            # this run daily
    #parse_symbols()        # this get all symbols in above file