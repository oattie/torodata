import pandas as pd

def read_csv_file():
	df = pd.read_csv("data/ptt.csv",index_col="Date",parse_dates=True)
	df.drop(columns=["Close"], inplace=True)
	df.rename(columns={"Date":"date","Open":"open","High":"high","Low":"low","Close":"close","Volume":"volume","Adj Close":"close"}, inplace=True)
	df['dividend']=0.0
	df['split']=1.0
	df.to_csv("zipline/daily/ptt.csv")

if __name__ == "__main__":
	read_csv_file()
