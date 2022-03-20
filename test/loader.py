import graph
import pandas as pd

def load_csv(direction):
    data = pd.read_csv(direction)
    return data



'''
#data_kospi = pd.read_csv("data/KOSPI Historical Data.csv")
#data_kospi = pd.read_csv("data/KOSPI Historical Data.csv",index_col = 1, dtype = {"ID": int, "LAST_NAME": str, "AGE": float})

data_kospi = pd.read_csv("data/KOSPI Historical Data.csv",index_col = 1, dtype = {"Date": str, "Price": str})

data_kospi = pd.read_csv("data/KOSPI Historical Data.csv", dtype = {"Date": str, "Price": str})


#print(data_kospi["Date"])
#print(data_kospi['Date'])




data = load_csv("data/KOSPI Historical Data.csv")
'''