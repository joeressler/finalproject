from ingredient import *
from level import *
from random import random

class Game:
    def __init__(self, config):
        """[Creating a potion mixing minigame simulator.]

        Args:
            config ([json]): [json file for game configuration]
        """
        self.levels = []
        for level in config:
            self.levels.append(Level(level, self))
        self.tokenswon = 0
        self.totaldrops = 0
        gameweight = sum(map(lambda x: x.levelweight, self.levels))
        cumulativeprob = 0
        for level in self.levels:
            for ing in level.ingredients:
                ing.prob = ing.weight / gameweight
                cumulativeprob += ing.prob
                ing.cprob = cumulativeprob
        
    def __repr__(self):
        return "Levels: %s \nTokens won: %u \nTotal drops: %u" % (self.levels, self.tokenswon, self.totaldrops)
    
    def singleDrop(self):
        """code to get a single dropped ingredient
        """
        rand = random()
        for level in self.levels:
            for ing in level.ingredients:
                if rand <= ing.cprob:
                    return ing
    
    def applyDrop(self, drop):
        """[applies drop 'drop' to that drop's level and then checks if the level is complete]

        Args:
            drop ([Ingredient]): [a drop]
        """
        drop.Drop()
        if drop.level.check():
            drop.level.mixing()
        
    def singleRound(self):
        """code to play an entire round until the last level is completed at least once
        """
        while True:
            
            pass
            
        
    def isComplete(self):
        """if all of the levels have been completed at least once then returns True
        """
        for level in self.levels:
            if level.isFinished() == False:
                return False
    

