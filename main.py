#Python3

import random
#need to restore from db, then retrive then display
filename = "die.csv"
class stargeneration():
    mainworld=0
    atmosphere=0
    populus=0
    hydros=0
    gov=0
    techlevel=0
    lawlevel=0

    def __init__(self):
        self.data=open(filename,"r")
        self.mainworld=(random.randint(1,6) + random.randint(1,6) - 2)
        self.atmosphere=(random.randint(1,6) + random.randint(1.6) - 7 + self.mainworld)
        if self.mainworld == 0:self.atmosphere = 0
        self.hydros = (random.randint(1,6) + random.randint(1,6) - 7 + self.mainworld)
        self.populus=(random.randint(1,6) + random.randint(1,6) - 2)
        self.gov=(random.randint(1,6) + random.randint(1,6) - 7 + self.populus)
        self.lawlevel=(random.randint(1,6) + random.randint(1,6) - 7 + self.gov)


        self.info = {"dice roll": self.mainworld}
        self




#def generateClusters():
    #c = 0
    #cx = 0
    #cy = 0
    #cz = 0
    #rad = random.uniform(CLUSRADA, CLUSRADB)
    #num = random.uniform(NUMCLUSA, NUMCLUSB)
    #clusters.append((cx, cy, cz, rad, num))
    #c = 1
    #while c < NUMCB:
        # random distance from centre
        #dist = random.uniform(CLUSRAD, GALX)
        # any rotation- clusters can be anywhere
        #theta = random.random() * 360
        #cx = math.cos(theta * math.pi / 180.0) * dist
        #cy = math.sin(theta * math.pi / 180.0) * dist
        #cz = random.random() * GALZ * 2.0 - GALZ
        #rad = random.uniform(CLUSRADA, CLUSRADB)
        #num = random.uniform(NUMCLUSA, NUMCLUSB)
        # add cluster to clusters array
        #clusters.append((cx, cy, cz, rad, num))
        # process next
        #c = c+1
        #sran = 0
        #cran = 0





















