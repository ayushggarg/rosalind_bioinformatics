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


file = open("rosalind_splc.txt", "r")
data = file.read().split(">")
file.close()

data_set = []
for line in data:
    if (len(line) == 0):
        continue
    parts = line.split()
    dna = ''.join(parts[1:])
    data_set.append(dna)
dna = data_set[0]
introns_set = data_set[1:]

for introns in introns_set:
    dna = dna.replace(introns, '')
print (dna_translation(dna))