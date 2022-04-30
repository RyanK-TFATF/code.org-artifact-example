# Ryan Kelley, 2022 code.org 6-12 Curriculum Development Manager Example Artifact 

import random 

dnaBases = ["A", "G", "C", "T"]
# Adenine, Guanine, Cytosine, Thymine

dnaCodons = ["ATG", "TAG"]
# ATG is the START codon, TAG is one of the stop codons.  
# Codon information referenced here:  https://www.genome.gov/genetics-glossary/Codon and https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables#Inverse_DNA_codon_table

dnaSequence = "" 
# Create an empty string variable to store the DNA sequence. 

basesGenerated = 0
# Variable to count how many bases have been generated. 