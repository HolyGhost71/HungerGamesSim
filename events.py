import random

def meleeKill(tributes):
    
    if len(tributes) < 2:
        return tributes
    
    trib1 = random.choice(tributes)
    tributes.remove(trib1)
    
    trib2 = random.choice(tributes)
    tributes.remove(trib2)
    
    modesOfKill = [f"{trib1.name} breaks {trib2.name}'s neck in a fight",
                   f"{trib2.name} is beaten to death by {trib1.name}",
                   f"{trib1.name} gets in a brawl with {trib2.name}. {trib1.name} wins",
                   f"{trib2.name} gets in a brawl with {trib1.name}. {trib1.name} wins",
                   f"{trib1.name} pushes {trib2.name} off a cliff",
                   f"{trib1.name} crushes {trib2.name}'s head with a rock"
                   
                   ]
    
    print(random.choice(modesOfKill))
    
    trib1.playerKill()
    trib2.alive = False
    
    return tributes

def weaponKill (tributes):
    
    if len(tributes) < 2:
        return tributes
    
    tributesWithWeapons = []
    
    for tribute in tributes:
        if tribute.weapon != None:
            tributesWithWeapons.append(tribute)
        
    if len(tributesWithWeapons) == 0:
        return tributes
    
    trib1 = random.choice(tributesWithWeapons) 
    tributes.remove(trib1)
    
    trib2 = random.choice(tributes)
    tributes.remove(trib2)
        
    if trib1.weapon in ["Sword", "Knife", "Sickle"]:
        print (f"{trib1.name} stabs {trib2.name} using the {trib1.weapon}")
    elif trib1.weapon in ["Axe", "Hatchet"]:
        print (f"{trib1.name} swings {trib1.their} {trib1.weapon} into {trib2.name}'s chest")
    elif trib1.weapon in ["Mace"]:
        print (f"{trib1.name} crushes {trib2.name}'s skull with {trib1.their} {trib1.weapon}")
    elif trib1.weapon in ["Bow"]:
        print (f"{trib1.name} shoots {trib2.name} with a {trib1.weapon}")

    trib2.alive = False
    trib1.playerKill()
    
    return tributes
            
def suicide (tributes):
    trib = random.choice(tributes)
    tributes.remove(trib)
    
    print(f"{trib.name} kills {trib.themself}")
    
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
              f"{trib.name} styles {trib.their} hair",
              f"{trib.name} feels tired",
            ]
    
    print(random.choice(events))
    
def weaponEquip (tributes):
    
    weaponList = ["Sword","Axe","Sickle","Hatchet","Knife","Bow","Mace"]
    
    trib = random.choice (tributes)
    tributes.remove(trib)
    trib.weapon = random.choice(weaponList)
    
    if trib.weapon in ["Sword","Sickle","Hatchet","Knife","Bow","Mace"]:
        print (f"{trib.name} finds a {trib.weapon}")
    if trib.weapon in ["Axe"]:
        print (f"{trib.name} finds an {trib.weapon}")
    