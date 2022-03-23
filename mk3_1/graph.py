from matplotlib import pyplot as plt 
#from matplotlib import ticker as mticker
#import FinanceDataReader as fdr
class C_line:
    name = ""
    price = []

    def __init__(self, name, price):
        self.name = name
        self.price = price



class C_chart:
    lines = []
    
    def add(self,price,name = "default"):
        line = C_line(name,price)
        self.lines.append(line)
        
    def show(self):
        for line in self.lines:
            plt.plot(line.price, label=line.name)  
        plt.legend()          
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
