from ingredient import *

class Level:
    def __init__(self, config, game):
        """[creates a Level object that represents a completable level that requires certain ingredients.]

        Args:
            config ([dict]): [dictionary describing the attributes and Ingredients of a level.]
            game ([Game]): [the parent game of this Level.]
        """
        self.level = config['level']
        self.reward = config['reward']
        self.ingredients = []
        self.completions = 0
        self.levelweight = 0
        self.game = game
        for ingredient in config['ingredients']:
            self.ingredients.append(Ingredient(ingredient, self)) # I love .append(). I love it so much. .append() is my favorite function.
        self.levelweight = sum(map(lambda x: x.weight, self.ingredients))
            
    def __repr__(self):
        """[represent function]

        Returns:
            [str]: [A representation of the Level object and its variables/Ingredients.]
        """
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
        # A little note, I called this mixing because this whole
        # program was created initially with the example of a
        # 'potion' being created from 'ingredients' since that was
        # one of the minigames that my father had worked on when he
        # worked at a bingo/casino game company.
        # So, this is mixing the ingredients together :)
        self.completions += 1
        self.game.tokenswon += self.reward
        for ing in self.ingredients:
            ing.quantity -= 1