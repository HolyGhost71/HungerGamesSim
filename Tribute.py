class Tribute:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.kills = 0
        self.weapon = None
        
    def playerKill(self):
        self.kills += 1