
# Python to convert 
# altered DNA to protein 

import importlib

moduleName = input('DNA.txt') # users input
importlib.import_module(moduleName) # passing the moduleName variable to the lib module

inputfile ="DNA.txt"
f = open("DNA.txt", "r") # opening the file which is being read
seq = f.read() # reading the file

seq = seq.replace("\n", "") # replaces all instances of "\n" that are seq variable
seq = seq.replace("\r", "") # replaces all instances of "\r" that are stored in the seq variable

def translate(seq): # dictionary collection which is unordered, changeable and indexed
    if input == ['ATT', 'ATC', 'ATA']:
        "I"
    elif input == ['CCA', 'CCG', 'CTT', 'CTC', 'CTA', 'CTG']:
        "L"
    elif input == ['GTT', 'GTC', 'GTA', 'GTG']:
        "V"
    elif input == ['TTT', 'TTC']:
        "F"
    elif input == ['ATG']:
        "M"

    else: "X"

	table = { 
		'I': ['ATT', 'ATC', 'ATA'],
        'L': ['CCA', 'CCG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'V': ['GTT', 'GTC', 'GTA', 'GTG'],
        'F': ['TTT', 'TTC'],
        'M': ['ATG'],
	} 

	protein ="" #divisable by 3?****
	if len(seq)%3 == 0: 
		for i in range(0, len(seq), 3):
			codon = seq[i:i + 3] 
			protein+= table[codon] 
	return protein 

def mutate(): 
	find_a = seq.find('a')
    print(find_a) # identify the first occurrence of the lowercase letter 'a' in DNA.txt

    dna_upper = sequence.upper() # normalDNA.txt file must contain the same DNA sequence as DNA.txt with the 'a' changed to an 'A
    n_file = open("normalDNA.txt", "w") # Open the file and overwrite the content
    n_file.write(dna_upper) # writing to the text file
    n_file.close() #closing the file

    dna_T = sequence.replace("a", "T") # mutatedDNA.txt file must contain the same DNA sequence as DNA.txt with the 'a' changed to a 'T'
    m_file = open("mutatedDNA.txt", "w") # Open the file and overwrite the content
    m_file.write(dna_T) # writing to the text file
    m_file.close() #closing the file


def txtTranslate(): #calls the translate function to both 'mutatedDNA.txt' and 'normalDNA.txt'
    dnaT = translate(read_file('mutatedDNA.txt'))  
    dna_upper = translate(read_file('normalDNA.txt'))

    print(dnaT[1])
    print(dna_upper[1])
 