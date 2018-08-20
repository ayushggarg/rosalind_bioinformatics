import itertools


file = open("rosalind_lexf.txt", "r")
data = file.read().split("\n")
file.close()

alphabet = data[0]
n = int(data[1])

#alphabet = "A C G T"
#n =2
alphabet_set = []

for letter in alphabet:
	if(letter != " "):
		alphabet_set.append(letter)

combination = itertools.product(alphabet_set, repeat = n)
for c in combination:
	str1 = ''.join(c)
	print (str1)