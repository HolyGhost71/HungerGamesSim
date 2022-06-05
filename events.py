import random
            
def suicide (tributes, day):
    trib = random.choice(tributes)
    tributes.remove(trib)
    
    selfKills = [f"{trib.name} kills {trib.themself}",
                        f"{trib.name} falls off a cliff",
                        f"{trib.name} is electrocuted by the barrier and dies",
                        f"{trib.name} accidentally eats poison berries",
                        f"{trib.name} kills {trib.themself}",
                        ]
    
    print(random.choice(selfKills))
    
    trib.setDead(day)
    
    return tributes

def dayEvent (tributes):
    
    trib = random.choice(tributes)
    tributes.remove(trib)
    
    soloEvents = [f"{trib.name} collects fruit",
              f"{trib.name} thinks of home",
              f"{trib.name} cries",
              f"{trib.name} tries to find a place to sleep",
              f"{trib.name} hunts and eats a rabbit",
              f"{trib.name} locates a source of water",
              f"{trib.name} looks for shelter",
              f"{trib.name} starts a fire",
              f"{trib.name} picks grass",
              f"{trib.name} styles {trib.their} hair",
              f"{trib.name} feels tired",
            ]
    
    print(random.choice(soloEvents))
    
def nightEvent (tributes):
    
    trib = random.choice(tributes)
    tributes.remove(trib)
    
    events = [f"{trib.name} sleeps",
              f"{trib.name} thinks of home",
              f"{trib.name} cries",
              f"{trib.name} climbs a tree and sleeps",
              f"{trib.name} sips water",
              f"{trib.name} eats food",
              f"{trib.name} stays awake all night",
              f"{trib.name} is woken up by the sounds of other tributes",
              f"{trib.name} hopes for a sponsorship",
              f"{trib.name} plans {trib.their} next attack",
              f"{trib.name} receives food from a sponsor",
              f"{trib.name} hides in the shadows"
            ]
    
    print(random.choice(events))

def cornucopiaEvent (tributes):
    trib = random.choice(tributes)
    tributes.remove(trib)
    
    events = [f"{trib.name} grabs a backpack",
              f"{trib.name} runs away",
              f"{trib.name} sprints away",
              f"{trib.name} takes a step forward but turns and runs",
              f"{trib.name} grabs a bottle of water",
              f"{trib.name} snatches food",
              f"{trib.name} falls over",
              f"{trib.name} scouts ahead",
              f"{trib.name} watches the chaos",
            ]
    
    print(random.choice(events))
 
def weaponEquip (tributes, cornucopia):
    
    weaponList = ["Sword","Axe","Sickle","Hatchet","Knife","Bow","Mace", "Blowgun", "Spear", "Trident", "Baton", "Machete"]
    
    trib = random.choice (tributes)
    
    if trib.weapon == None:
        trib.weapon = random.choice(weaponList)
        
        if (cornucopia):
            if trib.weapon[0].upper() in ["A", "E", "I", "O", "U"]:
                print (f"{trib.name} finds an {trib.weapon}")
            else:
                print (f"{trib.name} finds a {trib.weapon}")
                
        if not cornucopia:
            if trib.weapon[0].upper() in ["A", "E", "I", "O", "U"]:
                print (f"{trib.name} recieves an {trib.weapon} from a sponsor")
            else:
                print (f"{trib.name} receives a {trib.weapon} from a sponsor")
             
def meleeKill(tributes, day):
    
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
                   f"{trib1.name} crushes {trib2.name}'s head with a rock"
                   
                   ]
    
    print(random.choice(modesOfKill))
    
    stealWeapon(trib1, trib2)
    
    trib1.playerKill()
    trib2.setDead(day)
    
    return tributes

def weaponKill (tributes, day):
    
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
    
    bladeKills = [f"{trib1.name} stabs {trib2.name} using {trib1.their} {trib1.weapon}",
                f"{trib1.name} cuts {trib2.name}'s eye out with {trib1.their} {trib1.weapon}",
                f"{trib1.name} hacks away at {trib2.name}'s body with {trib1.their} {trib1.weapon}",
                f"{trib1.name} decapitates {trib2.name} with {trib1.their} {trib1.weapon}"
                ]

    axeKills = [f"{trib1.name} swings {trib1.their} {trib1.weapon} into {trib2.name}'s chest",
               f"{trib1.name} chops {trib2.name}'s head off with the {trib1.weapon}",
               f"{trib1.name} decapitates {trib2.name} with the {trib1.weapon}",
               f"{trib1.name} chops {trib2.name}'s arms off with the {trib1.weapon}",
               f"{trib1.name} throws {trib1.their} {trib1.weapon} into {trib2.name}'s back"
               ]
    
    bluntKills = [f"{trib1.name} crushes {trib2.name}'s skull with {trib1.their} {trib1.weapon}",
                f"{trib1.name} whacks {trib2.name}'s head with {trib1.their} {trib1.weapon}",
                f"{trib1.name} breaks {trib2.name}'s ribs with the {trib1.weapon}",
                f"{trib1.name} strangles {trib2.name} with the handle of {trib1.their} {trib1.weapon}"
                ]
    
    rangeKills = [f"{trib1.name} shoots {trib2.name} with {trib1.their} {trib1.weapon}",
                f"{trib1.name} fires into {trib2.name}'s neck with {trib1.their} {trib1.weapon}",
                f"{trib1.name} shoots straight into {trib2.name}'s eye with the {trib1.weapon}"
                ]

    longWeaponKills = [f"{trib1.name} stabs {trib2.name} in the stomach with {trib1.their} {trib1.weapon}",
                f"{trib1.name} throws the {trib1.weapon}, killing {trib2.name}",
                f"{trib1.name} catches {trib2.name} in a net, then finishes {trib2.them} off with the {trib1.weapon}",
                f"{trib1.name} pins {trib2.name} to a tree by throwing the {trib1.weapon}",   
                ]
    

    if trib1.weapon in ["Sword", "Knife", "Sickle", "Machete"]:
        print (random.choice(bladeKills))
        
    elif trib1.weapon in ["Axe", "Hatchet"]:
        print (random.choice(axeKills))
        
    elif trib1.weapon in ["Mace", "Baton"]:
        print (random.choice(bluntKills))
        
    elif trib1.weapon in ["Bow", "Blowgun"]:
        print (random.choice(rangeKills))
        
    elif trib1.weapon in ["Spear", "Trident"]:
        print (random.choice(longWeaponKills))

    weaponBreak(trib1, tributes)
    stealWeapon(trib1, trib2)

    trib2.setDead(day)
    trib1.playerKill()
    
    return tributes

def weaponBreak(tribute,tributesList):
    randomInt = random.randint(1,5)
    if randomInt == 1 and len(tributesList) != 1:
        print(f"{tribute.name}'s {tribute.weapon} breaks")
        tribute.weapon == None
        
def stealWeapon(aliveTribute, deadTribute):
    if aliveTribute.weapon == None and deadTribute.weapon != None:
        aliveTribute.weapon = deadTribute.weapon
        print(f"{aliveTribute.name} steals {deadTribute.name}'s {deadTribute.weapon}")
        deadTribute.weapon = None