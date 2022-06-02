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
     
    # Game
    while (True):
        print("\n=====Next Day=====\n")
        while (len(tributes) > 1):
            randomInt = random.randint(1,10)
            if 1 <= randomInt <= 4:
                randomEvent(tributes)
            elif 5 <= randomInt <= 6:
                tributes = kill(tributes)
            elif randomInt == 7:
                tributes = suicide(tributes)
    
        for t in startingTributes:
            if t.alive == True:
                tributes.append(t)
                
        if len(tributes) == 1:
            break
                
    winner = tributes[0].name
    
    print(f"Winner of the Hunger games is: {winner}")
    print("\nNumber of kills per player: \n")
    
    for i in range (0,len(startingTributes)):
        print(f"{startingTributes[i].name}: {startingTributes[i].kills}")
    
if __name__ == "__main__":
    main()