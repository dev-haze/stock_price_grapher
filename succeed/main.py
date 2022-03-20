import graph
import FinanceDataReader as fdr

chart = graph.C_chart()
cmd = ""

while(cmd != 'quit'):
    cmd = input()

    if(cmd == 'add'):
        print("code : ")
        code = input()
        data = fdr.DataReader(symbol = code)
        chart.add(data['Open'])
    
    elif(cmd == 'show'):
        chart.show()

    
    

        
    elif(cmd == 'clear'):
        chart.init()

    elif(cmd == 'help'):
        print("quit : quit stock_grapher")
        print("add  : add stock_code to graph")
        print("show :  show graph")

    elif cmd == 'dev_example':
        print("030210 kt, 032640 lg, 005930 samsung")                          


'''
#variable = fdr.DataReader('code','start','end')
#variable = fdr.DataReader('code',)
chart = graph.C_chart()

data = fdr.DataReader(symbol = '005930', start = '2020/01/01')#
chart.add(data['Open'])

data = fdr.DataReader(symbol = '032640', start = '2020/01/01')#
chart.add(data['Open'])



chart.show()
'''
