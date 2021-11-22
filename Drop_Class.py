class Drop:
    def __init__(self, name, p1, p2, p3, p4):
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    def __repr__(self):
        
        s1 = self.name + "\nP(1):" + str(int(self.p1 * 100)) + "% \nP(2):" + str(int(self.p2 * 100)) + "% \nP(3):" + str(int(self.p3 * 100)) + "% \nP(4):" + str(int(self.p4 * 100)) + "%"
        return s1
