import random

def createTributeArray() -> str:
    inputMode = input("(T)ext file or (M)anual: ")
        
    if (inputMode.lower().strip() == "t"):
        file = open("players.txt","r")
        text = file.read()
        tributes = text.split(", ")

    if (inputMode.lower().strip() == "m"):
        while (True):
            newTribute = ""
            newTribute = input("Tribute name, type EXIT when you are done: ")
            if (newTribute.lower().strip() == "exit"):
                break
            tributes.append(newTribute.lower().strip().capitalize())
            
    return tributes

def main():
    tributes = createTributeArray()

    # Game
    while (len(tributes) > 1):
        trib1 = random.choice(tributes)
        tributes.remove(trib1)
        
        trib2 = random.choice(tributes)
        tributes.remove(trib2)
        
        print(f"{trib1} kills {trib2}")
        
        tributes.append(trib1)
        
    winner = tributes[0]
    print(f"Winner of the Hunger games is: {winner}")
    
if __name__ == "__main__":
    main()