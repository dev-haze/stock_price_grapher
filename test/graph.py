from matplotlib import pyplot as plt 
from matplotlib import ticker as mticker

#plt.plot(date,price,color)
#plt.plot([1,2,3,4,5],[1,3,2,5,4],'r')
#plt.axis([xmin, xmax, ymin, ymax])
#plt.axis([0, 10, 0, 10])

#plt.show()



class C_line:
    date = []
    price = []
    def init(self,date,price):
        self.date = date
        self.price = price
        

class C_chart:
    lines = []
       
    def add(self, date,price):
        line = C_line()
        line.init(date,price)
        self.lines.append(line)

    def draw_graph(self):
        for line in self.lines:
            plt.plot(line.date,line.price)            
        plt.show()

    def init(self):
        self.lines.clear()
'''        
chart = C_chart()
chart.add([1,2,3],[2,5,3]) 
chart.add([1,2,3],[1,7,6]) 
chart.draw_graph()
'''