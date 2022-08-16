class Summary:
    def __init__(self):
        self.storage = {}

    def add(self, metrics, value):
        self.storage.setdefault(metrics, [])
        if value is not None:
            self.storage[metrics].append(value)

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
        with open('logs.txt', 'a') as fout:
            fout.write(s + '\n')
        print(s)

    def summaryWrite(self):
        s = '-------summary-------\n' \
            'average attempt: {}, ' \
            'average break: {}, ' \
            'average price: {:.2f}, '\
            'max, min attempt: {}, {}' \
            'max, min break: {}, {}' \
            'max, min price: {:.2f}, {:.2f} '\
            .format(self.get_average('attempt'),
                    self.get_average('break'),
                    self.get_average('price'),
                    self.get_maximum('attempt'), self.get_minimum('attempt'),
                    self.get_maximum('break'), self.get_minimum('break'),
                    self.get_maximum('price'), self.get_minimum('price'),
                    )
        with open('logs.txt', 'a') as fout:
            fout.write(s + '\n')
        print(s)

    def iteminfoWrite(self, level, initStars, targetStars):
        s = 'item level: {}, ' \
            'initial stars: {}, ' \
            'target stars: {}' \
            .format(level,
                    initStars,
                    targetStars
                    )
        with open('logs.txt', 'a') as fout:
            fout.write(s + '\n')
        print(s)

    def clear(self):
        self.storage.clear()