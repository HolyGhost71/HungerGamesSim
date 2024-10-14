import math
import random
from Tribute import Tribute
from events import *
from event_pools import *

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

def trigger_random_event(tributes, day, cycle, startingTributes):
    event_pool, event_weights = get_event_pool(cycle, tributes, startingTributes)
    
    # Select a random event based on weights
    event_function = random.choices(event_pool, weights=event_weights, k=1)[0]
    
    # Some events might return updated tributes (e.g., after kills)
    result = event_function(tributes, day)
    if result:
        tributes = result  # Update tributes if event function returns them
    
    return tributes

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
            
            # Trigger random event from the selected pool with weights
            tributes = trigger_random_event(tributes, dayNo, cycle, startingTributes)

        # Repopulates tribute array    
        tributes = [t for t in startingTributes if t.alive]
                  
        if len(tributes) == 1:
            break
  
        if cycle % 2 == 1:
            print("\nThe Fallen: ")
            for t in startingTributes:
                if not t.alive and t.deathDay == dayNo:
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