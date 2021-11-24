class Ingredient:
    def __init__(self, config, level):
        self.name = config['name']
        self.weight = config['weighting']
        self.quantity = 0
        self.prob = 0
        self.cprob = 0
        self.level = level

    def __repr__(self):
        return "%s %f" % (self.name, self.weighting)
    
    def Drop(self):
        self.quantity += 1
    
    def isAdded(self):
        """code that says if the level is finished
        """
        return self.quantity > 0