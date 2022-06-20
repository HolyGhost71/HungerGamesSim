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

def dayEvent (tributes, aliveTributes):

    randomInt = random.randint(1,35)
    
    if 29 < randomInt <= 35 and len(aliveTributes) > 6:
        if len(tributes) < 3: randomInt = random.randint(1,29)
        else:
            trib1 = random.choice(tributes)
            tributes.remove(trib1)
            trib2 = random.choice(tributes)
            tributes.remove(trib2)
            trib3 = random.choice(tributes)
            tributes.remove(trib3)
            trioEvents = [f"{trib1.name}, {trib2.name} and {trib3.name} set up camp",
                          f"{trib1.name}, {trib2.name} and {trib3.name} go hunting for tributes",
                          f"{trib1.name}, {trib2.name} and {trib3.name} go hunting for animals",
                          f"{trib1.name} is chased by {trib2.name} and {trib3.name} but escapes",
                          f"{trib1.name} and {trib2.name} steal from {trib3.name}'s supplies",
                          f"{trib1.name}, {trib2.name} and {trib3.name} argue with each other",]
            print(random.choice(trioEvents))
            return tributes
            
    if 17 < randomInt <= 29 and len(aliveTributes) > 4:
        if len(tributes) < 2: randomInt = random.randint(1,17)
        else:
            trib1 = random.choice(tributes)
            tributes.remove(trib1)
            trib2 = random.choice(tributes)
            tributes.remove(trib2)
            duoEvents = [f"{trib1.name} and {trib2.name} hunt for food",
                         f"{trib1.name} and {trib2.name} tell stories from home",
                         f"{trib1.name} tries to kill {trib2.name} but fails",
                         f"{trib1.name} injures {trib2.name}",
                         f"{trib1.name} steals supplies from {trib2.name}",
                         f"{trib1.name} and {trib2.name} have an arm wrestle, {trib1.name} wins",
                         f"{trib1.name} and {trib2.name} talk about their districts",
                         f"{trib1.name} and {trib2.name} make out in a cave",
                         f"{trib1.name} diverts {trib2.name}'s attention and runs away",
                         f"{trib1.name} and {trib2.name} hunt for other tributes",
                         f"{trib1.name} and {trib2.name} talk about the tributes still alive",
                         f"{trib1.name} defeats {trib2.name} but spares {trib2.their} life",]
            print(random.choice(duoEvents))
            return tributes
        
    else:
        trib1 = random.choice(tributes)
        tributes.remove(trib1)
        soloEvents = [f"{trib1.name} collects fruit",
              f"{trib1.name} thinks of home",
              f"{trib1.name} cries",
              f"{trib1.name} tries to find a place to sleep",
              f"{trib1.name} hunts and eats a rabbit",
              f"{trib1.name} locates a source of water",
              f"{trib1.name} looks for shelter",
              f"{trib1.name} starts a fire",
              f"{trib1.name} picks grass",
              f"{trib1.name} styles {trib1.their} hair",
              f"{trib1.name} feels tired",
              f"{trib1.name} does some pressups",
              f"{trib1.name} lays traps for other trib1utes",
              f"{trib1.name} picks wild berries",
              f"{trib1.name} does some pressups",
              f"{trib1.name} sees smoke in the distance",
              f"{trib1.name} discovers a cave",
            ]
        print(random.choice(soloEvents))
        return tributes
    
def nightEvent (tributes, aliveTributes):
    
    randomInt = random.randint(1,29)
    
    if 23 < randomInt <= 29 and len(aliveTributes) > 6:
        if len(tributes) < 3: randomInt = random.randint(1,23)
        else:
            trib1 = random.choice(tributes)
            tributes.remove(trib1)
            trib2 = random.choice(tributes)
            tributes.remove(trib2)
            trib3 = random.choice(tributes)
            tributes.remove(trib3)
            trioEvents = [f"{trib1.name}, {trib2.name} and {trib3.name} sleep in shifts",
                          f"{trib1.name}, {trib2.name} and {trib3.name} sleep in shifts",
                          f"{trib1.name}, {trib2.name} and {trib3.name} sleep in shifts",
                          f"{trib1.name}, {trib2.name} and {trib3.name} plan what to do the next day",
                          f"{trib1.name}, {trib2.name} and {trib3.name} cheerfully sing songs together",
                          f"{trib1.name}, {trib2.name} and {trib3.name} tell each other ghost stories",]
            print(random.choice(trioEvents))
            return tributes
            
    if 14 < randomInt <= 23 and len(aliveTributes) > 4:
        if len(tributes) < 2: randomInt = random.randint(1,14)
        else:
            trib1 = random.choice(tributes)
            tributes.remove(trib1)
            trib2 = random.choice(tributes)
            tributes.remove(trib2)
            duoEvents = [f"{trib1.name} and {trib2.name} snuggle",
                         f"{trib1.name} chases {trib2.name} but {trib2.they} escape",
                         f"{trib1.name} tends to {trib2.name}'s wounds",
                         f"{trib1.name} steals {trib2.name}'s supplies while {trib2.they} sleep",
                         f"{trib1.name} destroys {trib2.name}'s supplies while {trib2.they} sleep",
                         f"{trib1.name} lets {trib2.name} into {trib1.their} shelter",
                         f"{trib1.name} and {trib2.name} call a truce for the night",
                         f"{trib1.name} and {trib2.name} huddle for warmth",
                         f"{trib1.name} and {trib2.name} talk about the tributes still alive",]
            print(random.choice(duoEvents))
            return tributes
        
    else:
        trib1 = random.choice(tributes)
        tributes.remove(trib1)
        soloEvents = [f"{trib1.name} sleeps",
              f"{trib1.name} thinks of home",
              f"{trib1.name} cries",
              f"{trib1.name} climbs a tree and sleeps",
              f"{trib1.name} sips water",
              f"{trib1.name} eats food",
              f"{trib1.name} stays awake all night",
              f"{trib1.name} is woken up by the sounds of other tributes",
              f"{trib1.name} hopes for a sponsorship",
              f"{trib1.name} plans {trib1.their} next attack",
              f"{trib1.name} receives food from a sponsor",
              f"{trib1.name} hides in the shadows",
              f"{trib1.name} looks at the night sky",
              f"{trib1.name} is woken up by nightmares"
            ]
        
        print(random.choice(soloEvents))
        return tributes
    
def cornucopiaEvent (tributes):
    trib = random.choice(tributes)
    tributes.remove(trib)
    
    events = [f"{trib.name} grabs a backpack",
              f"{trib.name} runs away",
              f"{trib.name} runs away",
              f"{trib.name} runs away",
              f"{trib.name} sprints away",
              f"{trib.name} takes a step forward but turns and runs",
              f"{trib.name} grabs a bottle of water",
              f"{trib.name} snatches food",
              f"{trib.name} falls over",
              f"{trib.name} scouts ahead",
              f"{trib.name} watches the chaos",
              f"{trib.name} gathers as much food as {trib.they} can",
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
                   f"{trib1.name} overpowers {trib2.name} and kills {trib2.them}",
                   f"{trib1.name} crushes {trib2.name}'s head with a rock",
                   f"{trib1.name} bashes {trib2.name}'s head against a rock several times",
                   f"{trib1.name} ambushes {trib2.name} and kills {trib2.them}",
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
                f"{trib1.name} shoots {trib2.name}'s eye out with the {trib1.weapon}"
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
    if randomInt == 1 and len(tributesList)-1 != 1:
        print(f"{tribute.name}'s {tribute.weapon} breaks")
        tribute.weapon == None
        
def stealWeapon(aliveTribute, deadTribute):
    if aliveTribute.weapon == None and deadTribute.weapon != None:
        aliveTribute.weapon = deadTribute.weapon
        print(f"{aliveTribute.name} steals {deadTribute.name}'s {deadTribute.weapon}")
        deadTribute.weapon = None