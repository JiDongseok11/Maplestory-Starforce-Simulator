import math

SCALE = 100000000

class Price:
    
    def is_sale(self):
        return False

    def get_price(self, Level, currentStars):
        Level = int(Level/10)*10

        if Level < 10:
            price = 1000 + math.pow(Level, 3)*math.pow(currentStars+1,1)/25
        elif Level > 14:
            price = 1000 + math.pow(Level, 3)*math.pow(currentStars+1,2.7)/200
        else:
            price = 1000 + math.pow(Level, 3)*math.pow(currentStars+1,2.7)/400

        if not self.is_sale():
            return int(round(price, -2))

        else:
            return 0


# print("강화 비용 {:.2f}억 메소".format(get_price(150, 17)/SCALE))
    
