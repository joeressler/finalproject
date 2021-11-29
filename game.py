from ingredient import *
from level import *
import random

class Game:
    def __init__(self, config):
        """[Creating a potion mixing minigame simulator.]

        Args:
            config ([json]): [json file for game configuration]
        """
        self.levels = []
        for level in config:
            self.levels.append(Level(level, self)) # I love .append(). I love it so much. .append() is my favorite function.
        self.tokenswon = 0
        self.totaldrops = 0
        gameweight = sum(map(lambda x: x.levelweight, self.levels))
        self.cumulativeprob = 0
        for level in self.levels:
            for ing in level.ingredients:
                ing.prob = ing.weight / gameweight
                self.cumulativeprob += ing.prob
                ing.cprob = self.cumulativeprob
        
    def __repr__(self):
        """[represent function]

        Returns:
            [str]: [A representation of the Game object and its variables.]
        """
        # Le epic old-style formatting
        return "Levels: %s \nTokens won: %u \nTotal drops: %u \nCumulative probability: %.2f" % (self.levels, self.tokenswon, self.totaldrops, self.cumulativeprob)
    
    def singleDrop(self):
        """code to get a single dropped ingredient
        """
        rand = random.random()
        # Very inspired local variable is Very Inspired
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
        self.totaldrops += 1
        if drop.level.check():
            drop.level.mixing()
            # Epic usage of helper functions :)
        
    def singleRound(self):
        """code to play an entire round until the last level is completed at least once
        """
        while self.isComplete() == False:
            d = self.singleDrop()
            self.applyDrop(d)
            # Epic usage of helper functions :)

    # The self.reset() function ended up being useless after I decided to
    # create the Overlord object to manage iterating Games, but I'll keep
    # it here in case I need it later.
    def reset(self):
        """[code to reset the Game object after a game is completed.]
        """
        self.tokenswon = 0
        self.totaldrops = 0
        for level in self.levels:
            level.completions = 0
            for ing in level.ingredients:
                ing.quantity = 0   
        
    def isComplete(self):
        """if all of the levels have been completed at least once then returns True
        """
        for level in self.levels:
            if level.isFinished() == False:
                return False
                # Well, it's not finished, isFinished() certainly saw to that.
    

