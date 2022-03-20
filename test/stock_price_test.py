import FinanceDataReader as fdr

df_krx = fdr.StockListing('KOSPI')
print(df_krx.head())