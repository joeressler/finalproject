class Ingredient:
    def __init__(self, config, level):
        """[creates an Ingredient object that represents a droppable object for completing a given level.]

        Args:
            config ([dict]): [dictionary describing the attributes of an ingredient.]
            level ([Level]): [the parent Level of this Ingredient.]
        """
        self.name = config['name']
        self.weight = config['weighting']
        self.quantity = 0
        self.prob = 0
        self.cprob = 0
        self.level = level

    def __repr__(self):
        """[represent function]

        Returns:
            [str]: [A representation of the Ingredient object and its variables.]
        """
        return "\nName: %s, Probability: %0.2f%%" % (self.name, (self.prob * 100))
    
    def Drop(self):
        """[adds 1 to Ingredient.quantity]
        """
        self.quantity += 1
    
    def isAdded(self):
        """code that returns True if the ingredient has been added at least once 
        """
        return self.quantity > 0