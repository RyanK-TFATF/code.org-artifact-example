# Ryan Kelley, 2022 code.org 6-12 Curriculum Development Manager Non-Example Artifact, v1.0
# This example code will be used by the teacher to demonstrate an example of the same program that does not utilize lists. 

import random 

# DNA Bases
dnaBase0 = "A" # Adenine
dnaBase1 = "T" # Thymine
dnaBase2 = "G" # Guanine
dnaBase3 = "C" # Cytosine


# DNA Codons
dnaCodon0 = "ATG"
dnaCodon1 = "TAG"
dnaCodon2 = "GAT"
dnaCodon3 = "TTT"
dnaCodon4 = "AGC" 

# Create an empty string variable to store the DNA sequence. 
dnaSequence = "" 

# Variable to count how many bases have been generated. 
basesGenerated = 0

# Variable to control while loop, allows user to specify the number of bases to generate. 
requestedBases = int(input("How many DNA bases do you require in the sequence?  Type an integer value and press ENTER.\n"))

while basesGenerated <= requestedBases: # The teacher will specify how many bases to generate.  
    randomBase = int(random.randint(0,3)) # This simulates rolling the d4 to get a random number, start with 0 instead of 1 to ensure first element can be selected. 
    
    # if-elif-else to determine which base to add. 
    if randomBase == 0:
        nextBase = dnaBase0 # This references the first element in the dnaBases list. 
    elif randomBase == 2:
        nextBase = dnaBase1 # This references the second element in the dnaBases list. 
    elif randomBase == 3:
        nextBase = dnaBase2 # This references the third element in the dnaBases list. 
    else:
        nextBase = dnaBase3 # This references the fourth element in the dnaBases list. 
    
    dnaSequence += nextBase
    basesGenerated += 1 # Increment the number of bases generated. 
    
    
print(f"\nGenerated DNA Sequence: {dnaSequence}\n\n") # Print the sequence to verify proper generation. 

if dnaSequence.find(dnaCodon0) == -1: # .find() returns -1 if not found. 
    print(f"The {dnaCodon0} codon was NOT found in the generated sequence.\n")
else: 
    print(f"The {dnaCodon0} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodon0)}.\n") # Return the index of the first instance of the codon.  
if dnaSequence.find(dnaCodon1) == -1: # .find() returns -1 if not found. 
    print(f"The {dnaCodon1} codon was NOT found in the generated sequence.\n")
else: 
    print(f"The {dnaCodon1} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodon1)}.\n") # Return the index of the first instance of the codon.  
if dnaSequence.find(dnaCodon2) == -1: # .find() returns -1 if not found. 
    print(f"The {dnaCodon2} codon was NOT found in the generated sequence.\n")
else: 
    print(f"The {dnaCodon2} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodon2)}.\n") # Return the index of the first instance of the codon.  
if dnaSequence.find(dnaCodon3) == -1: # .find() returns -1 if not found. 
    print(f"The {dnaCodon3} codon was NOT found in the generated sequence.\n")
else: 
    print(f"The {dnaCodon3} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodon3)}.\n") # Return the index of the first instance of the codon.  
if dnaSequence.find(dnaCodon4) == -1: # .find() returns -1 if not found. 
    print(f"The {dnaCodon4} codon was NOT found in the generated sequence.\n")
else: 
    print(f"The {dnaCodon4} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodon4)}.\n") # Return the index of the first instance of the codon.  
    