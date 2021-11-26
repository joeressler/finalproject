from game import *
from statistics import mean

class Overlord:
    def __init__(self, gameconfig, simconfig):
        """[Overlord object to run games.]

        Args:
            gameconfig ([list]): [imported list from .json file]
            simconfig ([dict]): [dictionary key value created via user input]
        """
        self.config = gameconfig
        self.simconfig = simconfig
        self.tokenlist = []
        self.dropslist = []
        self.avgtokens = None
        self.avgdrops = None
    
    def __repr__(self):
        s1 = "Overlord object with file input gameconfig and user input simconfig \nCurrent average drops is " + str(self.avgdrops) + "\nCurrent average tokens is " + str(self.avgtokens)
        return s1
    
    def runGame(self):
        g1 = Game(self.config)
        g1.singleRound()
        return g1
    
    def runSims(self):
        for n in range(self.simconfig["number_runs"]):
            #print("Running game iteration %u" % (n))
            g1 = self.runGame()
            self.tokenlist.append(g1.tokenswon)
            self.dropslist.append(g1.totaldrops)
        print("Successfully ran %u times" % n)
        self.avgtokens = mean(self.tokenlist)
        self.avgdrops = mean(self.dropslist)
        worstcase = self.avgdrops * 2
        print("Average number of drops was %.2f" % self.avgdrops)
        print("Average number of tokens won was %.2f" % self.avgtokens)
        print("Maximum number of drops was %u" % max(self.dropslist))
        print("Number of users with worst case drops: %u" % sum(map(lambda x : 1 if x > worstcase else 0, self.dropslist)))
        
    
