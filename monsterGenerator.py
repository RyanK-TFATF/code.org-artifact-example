# Monster Generator, Ryan Kelley, v0.2b 
# This lesson focuses on demonstrating a method of creating random monsters in a game.  The code itself focuses on proper use of lists, while loops, methods, and code documentation.

# Module Imports -- Import critical modules first so they are available to the rest of your code. 
import random, time 

# MONSTER INFORMATION 

monsterType = [
    "Goblin",
    "Dragon", 
    "Zombie",
    "Orc",
    "Slime",
    "Skeleton"
]

monsterClass = [
    "Warrior",
    "Wizard",
    "Rogue",
    "Healer"    
]

monsterPrefix = [
    "Fire-Breathing",
    "Gargantuan",
    "Invisible",
    "Agitated",
    "Elite",
    "Confused"    
]

# Multiply the number of options from each category to get the total number of possible names.  
numPossible = len(monsterClass) * len(monsterType) * len(monsterPrefix) 

# Create an empty list to store the names. 
monsterNames = []


while len(monsterNames) < numPossible: # Execute the loop until we have generated all possible options. 

    # Randomly choose one of each option to create a new monster. 
    monsterPrefixGen = random.choice(monsterPrefix)    
    monsterTypeGen = random.choice(monsterType)    
    monsterClassGen = random.choice(monsterClass)     
         
    # Use string concatenation to create a new monster name. 
    newmonster = monsterPrefixGen + " " + monsterTypeGen  + " " + monsterClassGen 
    
    # Check to see if newmonster already exists in the list of names. 
    if newmonster in monsterNames: # If it's there, print an error message. 
        print("Monster Exists\n")
    else: # If it's not there, add it to the list.  
        monsterNames.append(newmonster)

# Sort the list. 
monsterNames.sort()    

# Print the list.  
print(monsterNames)
