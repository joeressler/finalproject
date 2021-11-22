class Drop:
    def __init__(self, config):
        self.name = config['name']
        self.p1 = config['p1']
        self.p2 = config['p2']
        self.p3 = config['p3']
        self.p4 = config['p4']
    def __repr__(self):
        
        s1 = self.name + "\nP(1):" + str(int(float(self.p1) * 100)) + "% \nP(2):" + str(int(float(self.p2) * 100)) + "% \nP(3):" + str(int(float(self.p3) * 100)) + "% \nP(4):" + str(int(float(self.p4) * 100)) + "%"
        return s1
