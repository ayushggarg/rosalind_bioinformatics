def dna_translation(dna):
    #print(dna_codon)
    prot = ""
    track = 0
    codon = dna[track:track+3]
    
    while (DNA_CODON_TABLE[codon] != "Stop"):
        prot += DNA_CODON_TABLE[codon]
        track += 3
        codon = dna[track:track+3]
        if (len(codon) <3):
            return 0
    return (prot)

def dna_compliment(dna):
    dna_comp = ""
    for letter in dna:
        if(letter == "A"):
            dna_comp += "T"
        elif(letter == "C"):
            dna_comp += "G"
        elif(letter == "G"):
            dna_comp += "C"
        elif(letter == "T"):
            dna_comp += "A"   
    return (dna_comp)

def start_sequences(dna):
    dna_codon = []
    reading_frame = 0
    while (reading_frame < 3):
        track = reading_frame
        reading_frame += 1
        codon = dna[track:track+3]
        
        while (track < len(dna)-3):
            if (codon == "ATG"):
                dna_codon.append(dna[track:])
            track += 3
            codon = dna[track:track+3]
    return (dna_codon)

DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}


file = open("rosalind_orf.txt", "r")
data = file.read().split(">")
file.close()

dna = ""
for line in data:
    parts = line.split()
    dna = ''.join(parts[1:])

prot = []
dna_comp = dna_compliment (dna)
dna_comp = dna_comp[::-1]

dna_start_seq = start_sequences(dna)
dna_comp_start_seq = start_sequences (dna_comp)


#print (dna_start_seq)
#print (dna_comp_start_seq)
#print ()

for i in range (len(dna_start_seq)):
    result =  dna_translation(dna_start_seq[i]) 
    if (result != 0):
        prot.append(result)

for i in range (len(dna_comp_start_seq)):
    result =  dna_translation(dna_comp_start_seq[i])
    if (result != 0):
        prot.append(result)

prot = set(prot)
for protein in prot:
    print (protein)