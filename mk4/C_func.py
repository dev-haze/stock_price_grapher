import graph
import FinanceDataReader as fdr

class C_stock:
    name=""
    code=""

class C_main:
    chart = graph.C_chart()
    cmd = ""
    stock_ls = []

    #create
    def __init__(self):
        stock = C_stock()
        self.stock_ls.append(stock)
    #------------------------------------   
    def add(self,code,name):
        stock = C_stock()
        stock.name = name
        stock.code = code
        self.stock_ls.append(stock)

    def delete(self,name):
        index = self.stock_ls.index(name)
        del self.stock_ls[index]
    
    def ls(self):
        print(self.stock_ls)
        
    def show(self):
        for stock in self.stock_ls:
            data = fdr.DataReader(symbol=stock.code)
            self.chart.add(data['Close'],stock.name)            
        self.chart.show()

    def clear(self):
        self.chart.init()

    def help():
        print("ls----------------: show stock list that was added by user")
        print("add (code) (name)-: add stock to graph")
        print("delete (name) ----: delete stock from stock list")
        print("show--------------: show graph")
        print("clear-------------: remove_all stock chart from canvas ")
        print("\n")
        print("quit--------------: quit stock_grapher")
        print("dev-examples------: print stock code examples")
    def ex(show):
        print("030210 kt")
        print("032640 kt")
        print("005930 kt")
                
            
    #------------------------------------
    
    def run(self):
        while(True):
            cmd = input()
            cmd = cmd.split()
            if cmd[0] == 'add':
                self.add(cmd[1],cmd[2])
            elif cmd[0] == 'del':
                self.delete(cmd[1])
            elif cmd[0] == 'show':
                self.chart.show()
            elif cmd[0] == 'clear':
                self.chart.init()
            elif cmd[0] == 'show':
                self.chart.show()
                
            elif cmd[0] == 'help':
                print("add (code) (name) : add stock_code to graph")
                print("show : show graph")
                print("quit : quit stock_grapher")
                print("dev-ex : print stock code examples")
            elif cmd[0] == 'q':
                break
            elif cmd[0]=='ex':
                self.ex()
            else: 
                continue
                




main = C_main()
main.run()