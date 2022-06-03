class Tribute:
    def __init__(self, name, gender):
        self.name = name
        self.alive = True
        self.kills = 0
        self.weapon = None
        self.deathDay = 0
        
        if gender == 'M':
            self.they = "he"
            self.them = "him"
            self.their = "his"
            self.themself = "himself"
            
        if gender == 'F':
            self.they = "she"
            self.them = "her"
            self.their = "her"
            self.themself = "herself"
            
        if gender == 'T':
            self.they = "they"
            self.them = "them"
            self.their = "their"
            self.themself = "themself"
        
    def playerKill(self):
        self.kills += 1
        
    def setDead(self, day):
        self.alive = False
        self.deathDay = day