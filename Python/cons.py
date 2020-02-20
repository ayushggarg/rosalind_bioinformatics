file = open("rosalind_cons.txt", "r")
data = file.read().split(">")
file.close()

parts =  (data[1]).split()
base = ''.join(parts[1:])
n = len(base)

profile_matrix = [[0 for x in range(n)] for x in range(4)]

for line in data:
	if len(line) == 0:
		continue

	parts = line.split()
	base = ''.join(parts[1:])

	for i in range(n):
		if (base[i] == 'A'):
			profile_matrix[0][i] += 1
		elif (base[i] == 'C'):
			profile_matrix[1][i] += 1
		elif (base[i] == 'G'):
			profile_matrix[2][i] += 1
		elif (base[i] == 'T'):
			profile_matrix[3][i] += 1

consensus = ""
for i in range(n):
	max_number = 0
	mex_index = 0
	for j in range(4):
		if (profile_matrix[j][i] > max_number):
			max_number = profile_matrix[j][i]
			max_index = j
	if (max_index == 0):
		consensus += 'A'
	elif (max_index == 1):
		consensus += 'C'
	elif (max_index == 2):
		consensus += 'G'
	elif (max_index == 3):
		consensus += 'T'

print (consensus)

profile_string_A = ' '.join(str(e) for e in profile_matrix[0])
profile_string_C = ' '.join(str(e) for e in profile_matrix[1])
profile_string_G = ' '.join(str(e) for e in profile_matrix[2])
profile_string_T = ' '.join(str(e) for e in profile_matrix[3])

print ("A: " + str(profile_string_A))
print ("C: " + str(profile_string_C))
print ("G: " + str(profile_string_G))
print ("T: " + str(profile_string_T))