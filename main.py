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
        
    for i in range (0,len(tributeNameArray)):
        objArray.append(Tribute(tributeNameArray[i]))
            
    return objArray

def main():
    #Preserves the original array of Tribute objects - shows dead/alive, kills etc.
    startingTributes = createTributeArray()
    #Only alive players are acted on
    tributes = startingTributes.copy()
    
    cycle: int = 2
     
    # Game
    while (True):
        
        if (cycle % 2 == 0): print("\n=== Day:",int(cycle/2),"===\n")
        else: print ("\n=== Night:", int((cycle-1)/2),"===\n")
        
        while (len(tributes) > 0):
            randomInt = random.randint(1,10)
            if 1 <= randomInt <= 2:
                randomEvent(tributes)
            elif 3 <= randomInt <= 4:
                tributes = weaponKill(tributes)
            elif 5 <= randomInt <= 6:
                tributes = meleeKill(tributes)
            elif randomInt == 7:
                tributes = suicide(tributes)
            elif randomInt == 8:
                weaponEquip(tributes)
            
    
        for t in startingTributes:
            if t.alive == True:
                tributes.append(t)
                
        if len(tributes) == 1:
            break
        
        cycle += 1
                
    winner = tributes[0].name
    
    print(f"Winner of the Hunger games is: {winner}")
    print("\nNumber of kills per player: \n")
    
    for i in range (0,len(startingTributes)):
        print(f"{startingTributes[i].name}: {startingTributes[i].kills}")
    
if __name__ == "__main__":
    main()