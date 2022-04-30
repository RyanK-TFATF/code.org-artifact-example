# Ryan Kelley, 2022 code.org 6-12 Curriculum Development Manager Example Artifact 

import random 

dnaBases = ["A", "G", "C", "T"]
# Adenine, Guanine, Cytosine, Thymine

dnaCodons = ["ATG", "TAG", "GAT", "TTT"]
# ATG is the START codon, TAG is one of the stop codons.  
# Codon information referenced here:  https://www.genome.gov/genetics-glossary/Codon and https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables#Inverse_DNA_codon_table

dnaSequence = "" 
# Create an empty string variable to store the DNA sequence. 

basesGenerated = 0
# Variable to count how many bases have been generated. 

while basesGenerated <= 100: # The teacher will specify how many bases to generate.  
    randomBase = int(random.randint(1,4)) # This simulates rolling the d4 to get a random number. 

    if randomBase == 1:
        nextBase = dnaBases[0] # This references the first element in the dnaBases list. 
    elif randomBase == 2:
        nextBase = dnaBases[1] # This references the second element in the dnaBases list. 
    elif randomBase == 3:
        nextBase = dnaBases[2] # This references the third element in the dnaBases list. 
    else:
        nextBase = dnaBases[3] # This references the fourth element in the dnaBases list. 
    
    dnaSequence += nextBase # Add the generated base to the dnaSequence string.  
    basesGenerated += 1 # Increment the number of bases generated. 

print(dnaSequence) # Print the sequence to verify proper generation. 

"""
if dnaSequence.find(dnaCodons[0]) == -1: # .find() returns -1 if not found. 
    print(f"The {dnaCodons[0]} codon was NOT found in the generated sequence.\n")
else: 
    print(f"The {dnaCodons[0]} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodons[0])}.\n") # Return the index of the first instance of the codon.  

if dnaSequence.find(dnaCodons[1]) == -1:
    print(f"The {dnaCodons[1]} codon was NOT found in the generated sequence.\n")
else: 
    print(f"The {dnaCodons[1]} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodons[1])}.\n")
"""

for i in range(0, len(dnaCodons)):
    if dnaSequence.find(dnaCodons[i]) == -1: # .find() returns -1 if not found. 
        print(f"The {dnaCodons[i]} codon was NOT found in the generated sequence.\n")
    else: 
        print(f"The {dnaCodons[i]} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodons[i])}.\n") # Return the index of the first instance of the codon.  
    """
    if dnaSequence.find(dnaCodons[i]) == -1:
        print(f"The {dnaCodons[i]} codon was NOT found in the generated sequence.\n")
    else: 
        print(f"The {dnaCodons[i]} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodons[i])}.\n")
    """ 
