from simulator import Simulator
from summary import Summary

CYCLE = 10
FILENAME = 'probability_table.txt'
TARGETSTARS = 22
LEVEL = 160
STARS = 0
SCALE = 100000000

simulator = Simulator(itemLevel = LEVEL, 
                      initStars = STARS, 
                      targetStars = TARGETSTARS
                      )

summary = Summary()

summary.iteminfoWrite(simulator.itemLevel, simulator.initStars, simulator.targetStars)

for episode in range(CYCLE):
    print("Episode: {}".format(episode + 1))
    simulator.do_simulation()

    summary.add('attempt', simulator.item.get_tryNum())
    summary.add('break', simulator.item.get_breakNum())
    summary.add('price', simulator.upgrader.totalPrice/SCALE)

    summary.episodeWrite(episode)

    simulator.reset()

summary.summaryWrite()
# with open('log.txt', 'r') as fin:
    