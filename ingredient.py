class Ingredient:
    def __init__(self, config, level):
        self.name = config['name']
        self.weight = config['weighting']
        self.quantity = 0
        self.prob = 0
        self.cprob = 0
        self.level = level

    def __repr__(self):
        return "\nName: %s, Probability: %0.2f%%" % (self.name, (self.prob * 100))
    
    def Drop(self):
        self.quantity += 1
    
    def isAdded(self):
        """code that returns True if the ingredient has been added at least once 
        """
        return self.quantity > 0