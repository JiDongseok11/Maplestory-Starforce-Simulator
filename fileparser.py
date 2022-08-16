FILENAME = 'probability_table.txt'

class Fileparser:
    
    def __init__(self, filename):
        self.filename = filename
        self.table = []
    
    def get_probTable(self):
        tempTable = []
        with open(self.filename, 'r') as file:
            for prob in file:
                tempTable.append(prob.strip('\n'))
        return tempTable

    def get_probability(self, stars):
        tables = self.get_probTable()
        self.table = tables[stars].split()
        self.table.remove(str(stars))
        for i in range(len(self.table)):
            self.table[i] = float(self.table[i].replace('%', ''))
        return self.table

"""   
Prob = Fileparser(FILENAME)
print(Prob.get_probability(12))
"""