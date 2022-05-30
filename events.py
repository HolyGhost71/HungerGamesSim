import random

def kill(tributes):
    trib1 = random.choice(tributes)
    tributes.remove(trib1)
    
    trib2 = random.choice(tributes)
    tributes.remove(trib2)
    
    print(f"{trib1.name} kills {trib2.name}")
    
    tributes.append(trib1)
    trib1.playerKill()
    
    return tributes

def suicide (tributes):
    trib1 = random.choice(tributes)
    tributes.remove(trib1)
    
    print(f"{trib1.name} kills themself")
    
    return tributes