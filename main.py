from simulator import Simulator
from summary import Summary
from tqdm import tqdm

CYCLE = 10
FILENAME = 'probability_table.txt'
TARGETSTARS = 17
LEVEL = 160
STARS = 0
SCALE = 100000000

simulator = Simulator(itemLevel = LEVEL, 
                      initStars = STARS, 
                      targetStars = TARGETSTARS
                      )

summary = Summary()

summary.iteminfoWrite(simulator.itemLevel, simulator.initStars, simulator.targetStars)

for episode in tqdm(range(CYCLE), desc = 'simulation process', unit = 'episodes', mininterval = 0.01):
    simulator.do_simulation()

    summary.add('attempt', simulator.item.get_tryNum())
    summary.add('break', simulator.item.get_breakNum())
    summary.add('price', simulator.upgrader.totalPrice/SCALE)
    summary.addGraph(simulator.upgrader.totalPrice/SCALE)
    
    summary.episodeWrite(episode)

    simulator.reset()

summary.summaryWrite()
summary.graphWrite()
# with open('log.txt', 'r') as fin:
    