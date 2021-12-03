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
        """[represent function]

        Returns:
            [str]: [A representation of the Overlord object and its variables.]
        """
        s1 = "Overlord object with file input gameconfig and user input simconfig \nCurrent average drops is " + str(self.avgdrops) + "\nCurrent average tokens is " + str(self.avgtokens)
        return s1
    
    def runGame(self):
        """[Script to create and run a single game.]

        Returns:
            [Game]: [returns the result of a given game object after running through a full round.]
        """
        g1 = Game(self.config)
        # Very inspired local variable, I know.
        g1.singleRound()
        return g1
    
    def runSims(self):
        """[creates and runs self.simconfig["number_runs"] games
        and averages the drops and tokens won as well as the maximum
        number of drops. It also looks at a given "worst case" scenario
        of # of drops (2 * average) and tallies how many users of the
        total had to experience this worst case.
        """
        for n in range(self.simconfig["number_runs"]):
            #print("Running game iteration %u" % (n))
            # This print line here is an artifact from testing
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
        
    
