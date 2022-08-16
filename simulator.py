from upgrader import *
from item import *
from fileparser import Fileparser

CYCLE = 1
FILENAME = 'probability_table.txt'
TARGETSTARS = 22
LEVEL = 160
STARS = 0
SCALE = 100000000

class Simulator:

    def __init__(self, 
                 itemLevel, 
                 initStars = 0, 
                 targetStars = 0, 
                 initIschance = False
                 ):

        self.itemLevel = itemLevel
        self.initStars = initStars
        self.targetStars = targetStars
        self.initIschance = initIschance

        self.item = Item(
            itemLevel = self.itemLevel, 
            initStars = self.initStars, 
            initIschance = self.initIschance
            )

        self.upgrader = Upgrader(
            Item = self.item,
            targetStars = self.targetStars
        )
        
    def reset(self):
        self.item.reset()
        self.upgrader.totalPrice = 0

    def do_simulation(self):
        if self.upgrader.do_upgrade():
            return True