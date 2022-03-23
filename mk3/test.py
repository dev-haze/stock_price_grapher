import graph
import FinanceDataReader as fdr
#git_test
chart = graph.C_chart()#만들어 놓은 graph.py 객체 생성
cmd = ""#input받은거 넣어둘 변수


while(True): #quit이 입력되면 바로 종료. 그렇지 않으면 계속 루프
    cmd = input()
    cmd = cmd.split()

    #<주요 명령어들>---------------
    if(cmd[0] == 'add'):#종목코드 입력 & 종목 그래프 따오기
        print("add 종목코드 종목명")
        data = fdr.DataReader(symbol = cmd[1])
        chart.add(data['Close'],cmd[2])
        #print(data['Open'])
        print(data)
    
    elif(cmd[0] == 'show'): #그래프 그리기
        chart.show()
        
    elif(cmd[0] == 'clear'):#차트 초기화
        chart.init()
    
        


    #<기타>-----------------------------
    elif(cmd[0] == 'help'):
        print("quit : quit stock_grapher")
        print("add (code) (name)  : add stock_code to graph")
        print("show :  show graph")

    elif cmd[0] == 'dev_ex':
        print("030210 kt, 032640 lg, 005930 samsung")                          

    elif cmd[0] == 'quit':
        break


'''
넣었으면 하는 기능:
차트에서 선택 종목 빼기
차트에 종목 이름 넣기


#variable = fdr.DataReader('code','start','end')
#variable = fdr.DataReader('code',)
chart = graph.C_chart()

data = fdr.DataReader(symbol = '005930', start = '2020/01/01')#
chart.add(data['Open'])

data = fdr.DataReader(symbol = '032640', start = '2020/01/01')#
chart.add(data['Open'])



chart.show()
'''
    