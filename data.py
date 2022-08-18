import matplotlib.pyplot as plt

datas = []

with open('./graph/2022-08-16T14:39:34.840773 graph.txt', 'r') as fopen:
    for line in fopen:
        datas.append(list(map(float, line.split(' '))))
    
xAxis = []
yAxis = []
for data in datas:
    xAxis.append(data[0])
    yAxis.append(data[1])
    
plt.plot(xAxis, yAxis)
plt.savefig('graph.png')