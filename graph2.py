from matplotlib import pyplot as plt 
from matplotlib import ticker as mticker
import FinanceDataReader as fdr

class C_line:
    price = []
    def init(self,price):
        self.price = price
        
class C_chart:
    lines = []
    color_ls = ['r','g','b','e35f62']
    counter = 0

    def add(self,price):
        #plt.plot(price, color = self.color_ls[self.counter])
        plt.plot(price)
        #self.counter += 1
        
    def show(self):            
        plt.show()

    def init(self):
        self.lines.clear()
        #self.counter = 0
'''        
chart = C_chart()
chart.add([1,2,3],[2,5,3]) 
chart.add([1,2,3],[1,7,6]) 
chart.draw_graph()
'''

#plt.plot(date,price,color)
#plt.plot([1,2,3,4,5],[1,3,2,5,4],'r')
#plt.axis([xmin, xmax, ymin, ymax])
#plt.axis([0, 10, 0, 10])

#plt.show()
