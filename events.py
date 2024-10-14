import random

            
def suicide (tributes, day):
    trib = random.choice(tributes)
    tributes.remove(trib)
    
    selfKills = [f"{trib.name} kills {trib.themself}",
                        f"{trib.name} falls off a cliff",
                        f"{trib.name} is electrocuted by the barrier and dies",
                        f"{trib.name} accidentally eats poison berries",
                        f"{trib.name} kills {trib.themself}",
                        f"{trib.name} falls into a ravine, disappearing into the abyss",
                        f"{trib.name} succumbs to their despair and swallows a fistful of poison berries",
                        f"{trib.name} runs head first into the barrier",
                        f"{trib.name} falls down a cliff while trying to climb it and dies on impact",
                        f"{trib.name} is eaten by a wild animal",
                        f"{trib.name} creates a fire so large that it consumes {trib.them}",
                        f"{trib.name} drowns in a river",
                        f"{trib.name} slips on a rock and breaks {trib.their} skull open",
                        f"{trib.name} dies from {trib.their} wounds",
                        f"{trib.name} is killed by a fireball sent by the gamemakers"
                        ]
    
    print(random.choice(selfKills))
    
    trib.setDead(day)
    
    return tributes

def dayEvent (tributes, day):

    randomInt = random.randint(1,35)
    
    if 29 < randomInt <= 35 and len(tributes) > 6:
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
                          f"{trib1.name}, {trib2.name} and {trib3.name} argue with each other",
                          f"{trib1.name}, {trib2.name}, and {trib3.name} ambush an unsuspecting tribute but fail to find them",
                          f"{trib1.name}, {trib2.name}, and {trib3.name} explore the outskirts of the arena, wary of traps",
                          f"{trib1.name}, {trib2.name}, and {trib3.name} gather around a small fire",
                          f"{trib1.name}, {trib2.name}, and {trib3.name} argue over supplies, tensions running high"
                          ]
            print(random.choice(trioEvents))
            return tributes
            
    if 17 < randomInt <= 29 and len(tributes) > 4:
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
                         f"{trib1.name} defeats {trib2.name} but spares {trib2.their} life",
                         f"{trib1.name} and {trib2.name} fight viciously over a scrap of food",
                         f"{trib1.name} helps {trib2.name} build a makeshift shelter from twigs and leaves",
                         f"{trib1.name} throws {trib2.name} into a trap, leaving them to die",
                         f"{trib1.name} and {trib2.name} wander the woods, looking for other tributes"
]
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
              f"{trib1.name} watches the horizon",
              f"{trib1.name} sharpens a stick into a makeshift weapon",
              f"{trib1.name} drinks from a small stream",
              f"{trib1.name} wanders if it would be good to have allies",
              f"{trib1.name} tries to camouflage {trib1.themself}",
              f"{trib1.name} looks for a way out of the arena",
              f"{trib1.name} appeals to the sponsors",
              f"{trib1.name} tries to remain hopeful"
            ]
        
        print(random.choice(soloEvents))
        return tributes
    
def nightEvent (tributes, day):
    
    randomInt = random.randint(1,29)
    
    if 23 < randomInt <= 29 and len(tributes) > 6:
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
                          f"{trib1.name}, {trib2.name} and {trib3.name} sleep in shifts. {trib2.name} considers betraying the rest",
                          f"{trib1.name}, {trib2.name} and {trib3.name} plan what to do the next day",
                          f"{trib1.name}, {trib2.name} and {trib3.name} cheerfully sing songs together",
                          f"{trib1.name}, {trib2.name} and {trib3.name} tell each other ghost stories",
                          f"{trib1.name}, {trib2.name}, and {trib3.name} cook a small meal",
                          f"{trib1.name}, {trib2.name}, and {trib3.name} debate strategies to survive the next day",
                          f"{trib1.name}, {trib2.name}, and {trib3.name} argue",
                          f"{trib1.name}, {trib2.name}, and {trib3.name} go their separate ways"
]
            
            print(random.choice(trioEvents))
            return tributes
            
    if 14 < randomInt <= 23 and len(tributes) > 4:
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
                         f"{trib1.name} and {trib2.name} talk about the tributes still alive",
                         f"{trib1.name} watches over {trib2.name} as {trib2.their} tend to {trib2.their} wounds",
                         f"{trib1.name} considers betraying {trib2.name} but decides to wait"
                         ]
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
              f"{trib1.name} is woken up by nightmares",
              f"{trib1.name} counts the stars",
              f"{trib1.name} builds a tiny fire but quickly puts it out, afraid of attracting attention",
              f"{trib1.name} sleeps",
              f"{trib1.name} falls out of the tree they are sleeping in",
              f"{trib1.name} stalks a tribute in the distance",
              f"{trib1.name} goes hunting for animals"
            ]
        
        print(random.choice(soloEvents))
        return tributes
    
def cornucopiaEvent (tributes, day):
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
              f"{trib.name} reaches for a weapon but gets scared and flees instead",
              f"{trib.name} grabs an empty backpack",
              f"{trib.name} snatches a bottle of medicine before anyone else can reach it",
              f"{trib.name} grabs a kit to make a trap"
            ]
    
    print(random.choice(events))
 
def weaponEquip (tributes, day):
    
    weaponList = ["Sword","Axe","Sickle","Hatchet","Knife","Bow","Mace", "Blowgun", "Spear", "Trident", "Baton", "Machete"]
    
    trib = random.choice (tributes)
    
    if trib.weapon == None:
        trib.weapon = random.choice(weaponList)
        
        if (day == 1):
            if trib.weapon[0].upper() in ["A", "E", "I", "O", "U"]:
                print (f"{trib.name} finds an {trib.weapon}")
            else:
                print (f"{trib.name} finds a {trib.weapon}")
                
        else:
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
                   f"{trib1.name} bites {trib2.name}'s throat open",
                   f"{trib2.name} is thrown off a cliff by {trib1.name}, dying on impact",
                   f"{trib1.name} wins a fight against {trib2.name}"
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
                f"{trib1.name} decapitates {trib2.name} with {trib1.their} {trib1.weapon}",
                f"{trib1.name} plunges {trib1.their} {trib1.weapon} into {trib2.name}'s chest, ending {trib2.their} life",
                f"{trib1.name} slashes {trib2.name} across the throat with a precise stroke using {trib1.their} {trib1.weapon}",


                ]

    axeKills = [f"{trib1.name} swings {trib1.their} {trib1.weapon} into {trib2.name}'s chest",
               f"{trib1.name} chops {trib2.name}'s head off with the {trib1.weapon}",
               f"{trib1.name} decapitates {trib2.name} with the {trib1.weapon}",
               f"{trib1.name} chops {trib2.name}'s arms off with {trib2.their} {trib1.weapon}",
               f"{trib1.name} throws {trib1.their} {trib1.weapon} into {trib2.name}'s back",
               f"{trib1.name} hacks {trib2.name}'s leg off with {trib1.their} {trib1.weapon}, watching {trib2.them} fall in agony",
               f"{trib1.name} hacks at {trib2.name} with {trib1.their} {trib1.weapon}, each strike more vicious than the last"
               ]
    
    bluntKills = [f"{trib1.name} crushes {trib2.name}'s skull with {trib1.their} {trib1.weapon}",
                f"{trib1.name} whacks {trib2.name}'s head with {trib1.their} {trib1.weapon}",
                f"{trib1.name} breaks {trib2.name}'s ribs with the {trib1.weapon}",
                f"{trib1.name} strangles {trib2.name} with the handle of {trib1.their} {trib1.weapon}",
                f"{trib1.name} bludgeons {trib2.name} into submission",
                f"{trib1.name} uses {trib1.their} {trib1.weapon} to break {trib2.name}'s bones, one by one"
                ]
    
    rangeKills = [f"{trib1.name} shoots {trib2.name} with {trib1.their} {trib1.weapon}",
                f"{trib1.name} fires into {trib2.name}'s neck with {trib1.their} {trib1.weapon}",
                f"{trib1.name} shoots {trib2.name}'s eye out with the {trib1.weapon}",
                f"{trib1.name} fires an arrow straight through {trib2.name}'s heart from a distance",
                f"{trib1.name} hits {trib2.name} in the eye with a deadly accurate shot",
                f"{trib2.name} is shot through the back of the head by {trib1.name} before {trib2.they} can process it",
                f"{trib1.name} fires a poison tipped projectile from {trib1.their} {trib1.weapon} at {trib2.name}"

                ]

    longWeaponKills = [f"{trib1.name} stabs {trib2.name} in the stomach with {trib1.their} {trib1.weapon}",
                f"{trib1.name} throws the {trib1.weapon}, killing {trib2.name}",
                f"{trib1.name} catches {trib2.name} in a net, then finishes {trib2.them} off with the {trib1.weapon}",
                f"{trib1.name} pins {trib2.name} to a tree by throwing the {trib1.weapon}",   
                f"{trib1.name} impales {trib2.name}, causing {trib2.them} to choke up blood"
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

def weaponBreak(tribute, day):
    randomInt = random.randint(1,5)
    if randomInt == 1:
        print(f"{tribute.name}'s {tribute.weapon} breaks")
        tribute.weapon = None
        
def stealWeapon(aliveTribute, deadTribute):
    if aliveTribute.weapon == None and deadTribute.weapon != None:
        aliveTribute.weapon = deadTribute.weapon
        print(f"{aliveTribute.name} steals {deadTribute.name}'s {deadTribute.weapon}")
        deadTribute.weapon = None