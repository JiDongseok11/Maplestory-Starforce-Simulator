from item import *
from price import get_price
import math
import random

SUCCESS = 1
FAIL = 0
BREAK = -1

class Upgrader:

    def __init__(self, Item, targetStars):
        self.targetStars = targetStars
        self.Item = Item
        self.totalPrice = 0

    def get_randNum(self):
        return random.randrange(1, 1000)

    def is_success(self):
        successProb = []
        failProb = []
        breakProb = []
        tempProb = []
        Prob = self.Item.get_currentProb()
        #확률 테이블을 편의를 위해 [1, 1000] range로 변경
        for prob in Prob:
            tempProb.append(int(prob*10))

        randNum = self.get_randNum() #randNum = [1, 1000]

        if randNum < tempProb[0]+1:
            return SUCCESS
        elif randNum < tempProb[0]+tempProb[1]+1:
            return FAIL
        else:
            return BREAK 

    def do_upgrade(self):
        while self.Item.currentStars != self.targetStars:
            self.totalPrice += get_price(self.Item.level, self.Item.currentStars)
            if self.Item.is_chance():
                isSuccess = SUCCESS
                #print("Chance Time!")
            else:
                isSuccess = self.is_success()
            if isSuccess == SUCCESS:
                self.Item.do_success()
            elif isSuccess == FAIL:
                self.Item.do_fail()
            else:
                self.Item.do_break()
            #print("Current Star: {}".format(self.Item.currentStars))
        return True



