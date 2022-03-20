from matplotlib import pyplot as plt 
from matplotlib import ticker as mticker

import pandas as pd

# Price를 float으로 못바꾼다고 하면 콤마(,) 지워주기(엑셀 등 프로그램 이용)
data_kospi = pd.read_csv("data/KOSPI Historical Data.csv",dtype = {"Date": str, "Price": float})
#data_kospi = pd.read_csv("data/KOSPI Historical Data.csv")


#data_kospi["Price"].apply(pd.to_numeric)

print(data_kospi["Price"])


plt.plot(data_kospi["Date"],data_kospi["Price"])
plt.show()

