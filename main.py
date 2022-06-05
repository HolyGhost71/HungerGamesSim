import math
import random
import numpy as np
from Tribute import Tribute
from events import *

def createTributeArray():
    objArray = []
    file = open("players.txt","r")
    text = file.read()
    tributeNameArray = text.split(", ")
    file.close()

    i = 0
    while i < len(tributeNameArray):
        objArray.append(Tribute(tributeNameArray[i], tributeNameArray[i+1]))
        i += 2
            
    return objArray

def main():
    #Preserves the original array of Tribute objects - shows dead/alive, kills etc.
    startingTributes = createTributeArray()
    #Only alive players are acted on
    tributes = startingTributes.copy()
    
    cycle: int = 2
     
    # Game
    while (True):
        
        if (cycle == 2): print("\n=== Cornucopia ===\n")
        elif (cycle % 2 == 0): print("\n=== Day:",int(cycle/2),"===\n")
        else: print ("\n=== Night:", int((cycle-1)/2),"===\n")
        
        dayNo = int(math.floor(cycle/2))
        
        while (len(tributes) > 0):
            
            # Cornucopia
            if cycle == 2:
                randomInt = random.randint(1,12)
                if 1 <= randomInt <= 5:
                    cornucopiaEvent(tributes)
                elif randomInt == 6:
                    tributes = meleeKill(tributes, dayNo)
                elif 7 <= randomInt <= 10:
                    weaponEquip(tributes, True)
                else:
                    tributes = weaponKill(tributes, dayNo)
                    
            # Day Endgame
            elif cycle % 2 == 0 and len(tributes) < len(startingTributes)/4:
                randomInt = random.randint(1,6)
                if 1 <= randomInt <= 3:
                    dayEvent(tributes)
                elif 4 <= randomInt <= 5:
                    tributes = weaponKill(tributes, dayNo)
                elif randomInt == 6:
                    tributes = meleeKill(tributes, dayNo)
                    
            # Night Endgame
            elif cycle % 2 == 0 and len(tributes) < len(startingTributes)/4:
                randomInt = random.randint(1,6)
                if 1 <= randomInt <= 4:
                    nightEvent(tributes)
                elif 5 <= randomInt <= 6:
                    tributes = weaponKill(tributes, dayNo)
                elif randomInt == 7:
                    tributes = meleeKill(tributes, dayNo)
                    
            # Day  
            elif cycle % 2 == 0:
                randomInt = random.randint(1,11)
                if 1 <= randomInt <= 5:
                    dayEvent(tributes)
                elif 6 <= randomInt <= 8:
                    tributes = weaponKill(tributes, dayNo)
                elif randomInt == 9:
                    tributes = meleeKill(tributes, dayNo)
                elif randomInt == 10:
                    tributes = suicide(tributes, dayNo)
                elif randomInt == 11:
                    weaponEquip(tributes, False)
                    
            # Night        
            elif cycle % 2 == 1:
                randomInt = random.randint(1,12)
                if 1 <= randomInt <= 6:
                    nightEvent(tributes)
                elif 7 <= randomInt <= 9:
                    tributes = weaponKill(tributes, dayNo)
                elif randomInt == 10:
                    tributes = meleeKill(tributes, dayNo)
                elif randomInt == 11:
                    tributes = suicide(tributes, dayNo)
                elif randomInt == 12:
                    weaponEquip(tributes, False)
            
        for t in startingTributes:
            if t.alive == True:
                tributes.append(t)
                  
        if len(tributes) == 1:
            break
  
        if cycle % 2 == 1:
            print("\nThe Fallen: ")
  
        for t in startingTributes:
            if t.alive == False and t.deathDay == dayNo and cycle % 2 == 1:
                print(t.name)
        
        cycle += 1
                
    winner = tributes[0].name
    
    print(f"\nWinner of the Hunger games is: {winner}")
    print("\nNumber of kills per player: \n")
    
    for t in startingTributes:
        if t.kills > 0:
            print(f"{t.name}: {t.kills}")
    
if __name__ == "__main__":
    main()