from ingredient import *

class Level:
    def __init__(self, config, game):
        self.level = config['level']
        self.reward = config['reward']
        self.ingredients = []
        self.completions = 0
        self.levelweight = 0
        self.game = game
        for ingredient in config['ingredients']:
            self.ingredients.append(Ingredient(ingredient, self))
        self.levelweight = sum(map(lambda x: x.weight, self.ingredients))
            
    
    def __repr__(self):
        return "\nLevel: %s \nReward: %s \nIngredients: %s \nTimes completed: %u\n" % (self.level, self.reward, self.ingredients, self.completions)
    
    def isFinished(self):
        """code that says if the level is finished
        """
        return self.completions > 0
    
    def check(self):
        """[A function that returns True if at least one every ingredient exists within the level and False otherwise]

        Returns:
            [bool]: [False if drop.isAdded() is False and True otherwise]
        """
        for drop in self.ingredients:
            if drop.isAdded() == False:
                return False
        return True
    
    def mixing(self):
        """[A function that completes the level and subtracts one from the ingredients in addition to adding the reward to total tokens won.]
        """
        self.completions += 1
        self.game.tokenswon += self.reward
        for ing in self.ingredients:
            ing.quantity -= 1