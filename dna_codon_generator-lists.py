# Ryan Kelley, 2022 code.org 6-12 Curriculum Development Manager Example Artifact, v1.0

# Import the random module to allow for random integer generation to simulate rolling the d4.
import random 

dnaBases = ["A", "G", "C", "T"]
# Adenine, Guanine, Cytosine, Thymine

dnaCodons = ["ATG", "TAG", "GAT", "TTT", "AGC"]
# ATG is the START codon, TAG is one of the stop codons.  
# Codon information referenced here:  https://www.genome.gov/genetics-glossary/Codon and https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables#Inverse_DNA_codon_table

# Create an empty string variable to store the DNA sequence. 
dnaSequence = "" 

# Variable to count how many bases have been generated. 
basesGenerated = 0

# Variable to control while loop, allows user to specify the number of bases to generate. 
requestedBases = int(input("How many DNA bases do you require in the sequence?  Type an integer value and press ENTER.\n"))

while basesGenerated < requestedBases: # The teacher will specify how many bases to generate.  
    dnaSequence += dnaBases[int(random.randint(0,3))] # This simulates rolling the d4 to get a random number, start with 0 instead of 1 to ensure first element can be selected. 
    basesGenerated += 1 # Increment the number of bases generated. 
    
print(f"\nGenerated DNA Sequence: {dnaSequence}\n\n") # Print the sequence to verify proper generation. 

for i in range(0, len(dnaCodons)):
    if dnaSequence.find(dnaCodons[i]) == -1: # .find() returns -1 if not found. 
        print(f"The {dnaCodons[i]} codon was NOT found in the generated sequence.\n")
    else: 
        print(f"The {dnaCodons[i]} codon was found!  The first instance starts at index {dnaSequence.find(dnaCodons[i])}.\n") # Return the index of the first instance of the codon.  
