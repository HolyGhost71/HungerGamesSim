import random

def kill(tributes):
    
    trib1 = random.choice(tributes)
    tributes.remove(trib1)
    
    trib2 = random.choice(tributes)
    tributes.remove(trib2)
    
    modesOfKill = [f"{trib1.name} kills {trib2.name}",
                   f"{trib1.name} breaks {trib2.name}'s neck in a fight",
                   f"{trib2.name} is killed by {trib1.name}",
                   f"{trib1.name} gets in a brawl with {trib2.name}. {trib1.name} wins",
                   f"{trib1.name} gets in a brawl with {trib2.name}. {trib2.name} wins",
                   f"{trib1.name} pushes {trib2.name} off a cliff",
                   
                   ]
    
    print(random.choice(modesOfKill))
    
    tributes.append(trib1)
    trib1.playerKill()
    trib2.setDead()
    
    return tributes

def suicide (tributes):
    trib1 = random.choice(tributes)
    tributes.remove(trib1)
    
    print(f"{trib1.name} kills themself")
    
    return tributes