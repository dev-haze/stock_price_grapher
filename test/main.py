dimport graph
import loader
import stock_price

stockClass = stock_price.C_stock()
stock = stockClass.search('005930','2020')
#print(stock['Open'])
print(stock.head())


'''
chart = graph.C_chart()
chart.add(stock['date'],stock['Open'])
chart.draw_graph()
'''

'''
data = loader.load_csv("data/KOSPI Historical Data.csv")
chart = graph.C_chart()
chart.add(data["Date"], data["Price"])
chart.draw_graph()
'''


