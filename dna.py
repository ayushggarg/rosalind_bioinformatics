file = open("rosalind_dna.txt", "r")
data = file.read()
file.close()

count_A = 0
count_C = 0
count_G = 0
count_T = 0
for letter in data:
	if (letter == "A"):
		count_A += 1
	elif (letter == "C"):
		count_C += 1
	elif (letter == "G"):
		count_G += 1
	elif (letter == "T"):
		count_T += 1

print (count_A, end = " ")
print (count_C, end = " ")
print (count_G, end = " ")
print (count_T)