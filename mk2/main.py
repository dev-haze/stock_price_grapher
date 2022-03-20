import graph
import FinanceDataReader as fdr
#git_test
chart = graph.C_chart()#만들어 놓은 graph.py 객체 생성
cmd = ""#input받은거 넣어둘 변수

while(cmd != 'quit'): #quit이 입력되면 바로 종료. 그렇지 않으면 계속 루프
    cmd = input()

    if(cmd == 'add'):#add가 입력되면
        print("code : ")
        code = input()#종목코드 입력받기
        data = fdr.DataReader(symbol = code)#해당 종목코드로 종목 검색
        chart.add(data['Open'])#차트에 선 추가
    
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
