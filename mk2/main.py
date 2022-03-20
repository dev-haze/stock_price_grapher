import graph
import FinanceDataReader as fdr
#git_test
chart = graph.C_chart()#만들어 놓은 graph.py 객체 생성
cmd = ""#input받은거 넣어둘 변수


while(True): #quit이 입력되면 바로 종료. 그렇지 않으면 계속 루프
    cmd = input()
    cmd = cmd.split()
    
    if(cmd[0] == 'add'):
        data = fdr.DataReader(symbol = cmd[1])
        chart.add(data['Open'])
    

    elif(cmd[0] == 'show'): 
        chart.show()
    
        
    elif(cmd[0] == 'clear'):
        chart.init()




    elif(cmd[0] == 'help'):
        print("quit : quit stock_grapher")
        print("add  : add stock_code to graph")
        print("show :  show graph")

    elif cmd[0] == 'dev_example':
        print("030210 kt, 032640 lg, 005930 samsung")                          

    elif cmd[0] == 'quit':
        break


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
