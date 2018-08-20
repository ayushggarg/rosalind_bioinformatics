file = open("rosalind_sseq.txt", "r")
data = file.read().split(">")
file.close()

data_set = []
for line in data:
    if (len(line) == 0):
        continue
    
    parts = line.split()
    temp = ''.join(parts[1:])
    data_set.append(temp)

string = data_set[0]
subsequence = data_set[1]

string_track = 0
subsequence_track = 0

while ((string_track < len(string)) and (subsequence_track < len(subsequence))):
	if (string[string_track] == subsequence[subsequence_track]):
		subsequence_track += 1
		print (string_track+1, end = " ")
	string_track += 1
print()

