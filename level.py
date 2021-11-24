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
        self.levelweight = sum(map(lambda x: x['weight'], self.ingredients))
        for ing in self.ingredients:
            self.levelweight += ing.weight
            
    
    def __repr__(self):
        return "%s %s %s" % (self.level, self.reward, self.ingredients)
    
    def isFinished(self):
        """code that says if the level is finished
        """
        return self.completions > 0
    
    def check(self):
        for drop in self.ingredients:
            if drop.isAdded() == False:
                return False
        return True
    
    def mixing(self):
        self.completions += 1
        self.game.tokenswon += self.reward
        for ing in self.ingredients:
            ing.quantity -= 1
