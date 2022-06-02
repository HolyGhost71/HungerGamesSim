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
                   f"{trib1.name} crushes {trib2.name}'s head with a rock"
                   
                   ]
    
    print(random.choice(modesOfKill))
    
    trib1.playerKill()
    trib2.alive = False
    
    return tributes

def suicide (tributes):
    trib = random.choice(tributes)
    tributes.remove(trib)
    
    print(f"{trib.name} kills themself")
    
    trib.alive = False
    
    return tributes

def randomEvent (tributes):
    
    trib = random.choice(tributes)
    tributes.remove(trib)
    
    events = [f"{trib.name} collects fruit",
              f"{trib.name} thinks of home",
              f"{trib.name} cries",
              f"{trib.name} finds for a place to sleep",
              f"{trib.name} hunts and eats a rabbit",
              f"{trib.name} locates a source of water",
              f"{trib.name} looks for shelter",
              f"{trib.name} starts a fire",
              f"{trib.name} picks grass",
              f"{trib.name} styles their hair",
              f"{trib.name} feels tired",
            ]
    
    print(random.choice(events))