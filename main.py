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



    def __init__(self):
        self.data=open(filename,"r")
        self.mainworld=(random.randint(1,6) + random.randint(1,6) - 2)
        self.atmosphere=(random.randint(1,6) + random.randint(1.6) - 7 + self.mainworld)
        if self.mainworld == 0:self.atmosphere = 0
        self.hydros = (random.randint(1,6) + random.randint(1,6) - 7 + self.mainworld)