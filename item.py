from fileparser import Fileparser
FILENAME = 'probability_table.txt'

class Item:

    def __init__(self, itemLevel, initStars = 0, initIschance = False):
        self.initStars = initStars #초기화용
        self.initIschance = initIschance
        self.currentStars = initStars #초기 아이템 스타포스 상태(int)
        self.isChance = initIschance #현재 찬스타임인지 여부(Bool)
        self.level = itemLevel #강화하는 아이템 레벨(int)
        self.tryNum = {} #각 스타포스당 강화 시도 횟수(dict{key(스타포스 수): int, value(강화 횟수): int))
        self.breakNum = 0 #장비 파괴 횟수
        self.checkChance = 0 #찬스타임 확인

        self.Fileparser = Fileparser(FILENAME)
        self.currentProb = self.Fileparser.get_probability(self.currentStars)

    def reset(self):
        self.currentStars = self.initStars
        self.isChance = self.initIschance
        self.currentProb = self.Fileparser.get_probability(self.currentStars)
        self.tryNum = {}
        self.breakNum = 0
        self.checkChance = 0
        return True

    def is_stay(self):
        if self.currentStars <= 10 or self.currentStars == 15 or self.currentStars == 20:
            return True
        else:
            return False
    
    def is_done(self, targetStars):
        return True if self.currentStars == targetStars else False

    def is_break_able(self):
        return True if self.currentStars >= 12 else False

    def is_chance(self):
        return True if self.checkChance == 2 else False

    def update_tryNum(self):
        try:
            self.tryNum[self.currentStars] += 1
        except:
            self.tryNum[self.currentStars] = 1


    def update_currentProb(self):
        self.currentProb = self.Fileparser.get_probability(self.currentStars)
        return True

    def do_success(self):
        self.update_tryNum()
        self.currentStars += 1
        self.update_currentProb()
        self.checkChance = 0
        #print('SUCCESS!')

    def do_fail(self):
        self.update_tryNum()
        if not self.is_stay():
            self.currentStars -= 1
            #찬스타임 로직 추가
            self.checkChance += 1
        self.update_currentProb()
        #print('FAIL')

    def do_break(self):
        self.update_tryNum()
        self.currentStars = 12
        self.breakNum += 1
        self.update_currentProb()
        self.checkChance = 0
        #print('BREAK...')

    def get_tryNum(self):
        return sum(list(map(int, self.tryNum.values())))

    def get_breakNum(self):
        return self.breakNum

    def get_currentProb(self):
        return self.currentProb

    def get_state(self):
        state = []
        state.append(self.currentStars)
        state.append(self.get_tryNum())
        state.append(self.get_breakNum())
        return state



