from datetime import datetime

class Summary:
    def __init__(self):
        self.storage = {}
        self.graph = {}
        self.name = './result/' + datetime.now().isoformat() + ' log.txt'
        self.graphname = './graph/' + datetime.now().isoformat() + ' graph.txt'

    def add(self, metrics, value):
        self.storage.setdefault(metrics, [])
        if value is not None:
            self.storage[metrics].append(value)
    
    def addGraph(self, price):
        try:
            self.graph[round(price, 1)] += 1
        except:
            self.graph[round(price, 1)] = 1

    def get_average(self, metrics):
        lst = self.storage[metrics]
        return None if len(lst) == 0 else sum(lst)/len(lst)

    def get_maximum(self, metrics):
        lst = self.storage[metrics]
        return None if len(lst) == 0 else max(self.storage[metrics])
    
    def get_minimum(self, metrics):
        lst = self.storage[metrics]
        return None if len(lst) == 0 else min(self.storage[metrics])

    def episodeWrite(self, episode):
        s = 'episode: {}, ' \
            'attempt: {}, ' \
            'break: {}, ' \
            'price: {:.2f} '\
            .format(episode + 1,
                    self.storage['attempt'][episode],
                    self.storage['break'][episode],
                    self.storage['price'][episode]
                    )
        with open(self.name, 'a') as fout:
            fout.write(s + '\n')
        #print(s)

    def summaryWrite(self):
        s = '-------summary-------\n' \
            'average attempt: {}\n' \
            'average break: {}\n' \
            'average price: {:.2f}\n'\
            'max, min attempt: {}, {}\n' \
            'max, min break: {}, {}\n' \
            'max, min price: {:.2f}, {:.2f}\n'\
            .format(self.get_average('attempt'),
                    self.get_average('break'),
                    self.get_average('price'),
                    self.get_maximum('attempt'), self.get_minimum('attempt'),
                    self.get_maximum('break'), self.get_minimum('break'),
                    self.get_maximum('price'), self.get_minimum('price'),
                    )
        with open(self.name, 'a') as fout:
            fout.write(s + '\n')
        print(s)

    def iteminfoWrite(self, level, initStars, targetStars):
        s = 'item level: {}, ' \
            'initial stars: {}, ' \
            'target stars: {}\n' \
            '-------episodes-------'\
            .format(level,
                    initStars,
                    targetStars
                    )
            
        with open(self.name, 'a') as fout:
            fout.write(s + '\n')
        print(s)
        
    def graphWrite(self):
        s = ''
        for key, value in self.graph.items():
            s += str(key) + ' ' + str(value) + '\n'
            
        with open(self.graphname, 'a') as fout:
            fout.write(s + '\n')

    def clear(self):
        self.storage.clear()