import matplotlib.pyplot as plt
from datetime import datetime


GRAPHTXT = './graph/2022-08-16T14:39:34.840773 graph.txt'
CYCLE = 10000

class Dataprocessing:
    def __init__(self, graphTxt, tryNum):
        self.runtime = './graph/' + datetime.now().isoformat() + ' '
        self.graphTxt = graphTxt #str filename
        self.graphDatas = []
        self.get_graphData()
        self.tryNum = tryNum
        
    def get_graphData(self):
        with open(self.graphTxt, 'r') as fopen:
            for line in fopen:
                self.graphDatas.append(list(map(float, line.split(' '))))
        self.graphDatas.sort()
        return self.graphDatas

    def get_graph(self):
        xAxis = []
        yAxis = []
        for data in self.graphDatas:
            xAxis.append(data[0])
            yAxis.append(data[1])

        plt.plot(xAxis, yAxis)
        plt.savefig(self.runtime + 'graph.png')
        
    def get_average_for_percent(self, per): #상위 n%까지의 평균 비용 보여주는 함수
        cnt = 0
        price = 0
        for data in self.graphDatas:
            cnt += int(data[1])
            price += data[0]
            if cnt/self.tryNum*100 > float(per):
            	break
        return price/cnt
    
    def get_price_for_percent(self, per):
        cnt = 0
        for data in self.graphDatas:
            cnt += int(data[1])
            if cnt/self.tryNum*100 > float(per):
                price = data[0]
                break
        return price
    
    def get_my_luck(self, cost):
        cnt = 0
        for data in self.graphDatas:
            if float(cost) <= data[0]:
                break
            cnt += int(data[1])
        return cnt/self.tryNum * 100
    
dp = Dataprocessing(GRAPHTXT, CYCLE)
#dp.get_graph()
#print("상위 60% 평균 비용: {:.02f}".format(dp.get_average_for_percent(60)))
#print("227.9억 메소를 쓴 경우 상위 {:.02f}%입니다".format(dp.get_my_luck(227.9)))
#print(dp.get_price_for_percent(60))
