import random
from Tribute import Tribute

def createTributeNameArray():
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
            
    return tributeNameArray

def createTributeObjectArray(names):
    objArray = []
    print(names)
    
    for i in range (0,len(names)):
        objArray.append(Tribute(names[i]))
    
    return objArray

def main():
    tributesNames = createTributeNameArray()
    tributes = createTributeObjectArray(tributesNames)
     
    # Game
    while (len(tributes) > 1):
        trib1 = random.choice(tributes)
        tributes.remove(trib1)
        
        trib2 = random.choice(tributes)
        tributes.remove(trib2)
        
        print(f"{trib1.name} kills {trib2.name}")
        
        tributes.append(trib1)
        
    winner = tributes[0].name
    print(f"Winner of the Hunger games is: {winner}")
    
if __name__ == "__main__":
    main()