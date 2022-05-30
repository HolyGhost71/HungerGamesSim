class Tribute:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.kills = 0
    
    def setDead(self):
        self.alive = False
        
    def playerKill(self):
        self.kills += 1
        
    