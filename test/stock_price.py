import FinanceDataReader as fdr


class C_stock:

    def search(self,code,start):
        df_kospi = fdr.StockListing('KOSPI')
        df = fdr.DataReader(code,start)
        return df

'''
stock = Stock()
company = stock.search('005930','2020')
print(company)
print(company['Open'])
'''
