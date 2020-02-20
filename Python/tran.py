def transition_transversion_count(s1, s2):
	trasitions = 0
	transversions = 0
	for i in range(len(s1)):
		if (s1[i] == s2[i]):
			continue
		elif ((s1[i] == "A" and s2[i] == "G") or (s1[i] == "G" and s2[i] == "A")):
			trasitions += 1
		elif ((s1[i] == "C" and s2[i] == "T") or (s1[i] == "T" and s2[i] == "C")):
			trasitions += 1
		else:
			transversions += 1
	return (trasitions/transversions)


file = open("rosalind_tran.txt", "r")
data = file.read().split(">")
file.close()

string_set = []
for line in data:
    if (len(line) == 0):
        continue
    
    parts = line.split()
    dna = ''.join(parts[1:])
    string_set.append(dna)

s1 = string_set[0]
s2 = string_set[1]

print (transition_transversion_count(s1, s2))
