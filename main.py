from decimal import ROUND_DOWN
import math
import random
import time
import numpy as np
from Tribute import Tribute
from events import *

def createTributeArray():
    objArray = []
    while (True):
        
        inputMode = input("(T)ext file or (M)anual: ")
        
        if (inputMode.lower().strip() == "t"):
            file = open("players.txt","r")
            text = file.read()
            tributeNameArray = text.split(", ")
            break

        if (inputMode.lower().strip() == "m"):
            tributeNameArray = []
            while (True):
                newTribute = ""
                newTribute = input("Tribute name, type EXIT when you are done: ")
                if (newTribute.lower().strip() == "exit"):
                    break
                tributeNameArray.append(newTribute.lower().strip().capitalize())
            break
        
        else: print("Invalid input")
        
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
                
            elif cycle % 2 == 0:
                randomInt = random.randint(1,11)
                if 1 <= randomInt <= 5:
                    dayEvent(tributes)
                elif 6 <= randomInt <= 8:
                    tributes = weaponKill(tributes, dayNo)
                elif randomInt == 9:
                    tributes = meleeKill(tributes, dayNo)
                elif randomInt == 10 and len(tributes) > 5:
                    tributes = suicide(tributes, dayNo)
                elif randomInt == 11:
                    weaponEquip(tributes, False)
                    
            elif cycle % 2 == 1:
                randomInt = random.randint(1,12)
                if 1 <= randomInt <= 6:
                    nightEvent(tributes)
                elif 7 <= randomInt <= 9:
                    tributes = weaponKill(tributes, dayNo)
                elif randomInt == 10:
                    tributes = meleeKill(tributes, dayNo)
                elif randomInt == 11 and len(tributes) > 5:
                    tributes = suicide(tributes, dayNo)
                elif randomInt == 12:
                    weaponEquip(tributes, False)
            
        for t in startingTributes:
            if t.alive == True:
                tributes.append(t)
                  
        if len(tributes) == 1:
            break
        
        if (cycle % 2 == 1):   
            print("\nThe Fallen:")  
        
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