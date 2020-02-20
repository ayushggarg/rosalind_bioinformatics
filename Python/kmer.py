import itertools

def mer_composition(string):
	composition_set = []
	for track in range(len(string)-3):
		comp = string[track:track+4]
		composition_set.append(comp)
	return (composition_set)


def lexicographical_composition():
	alphabet = "A C G T"
	n = 4
	alphabet_set = []
	lexicographical_set = []

	for letter in alphabet:
		if(letter != " "):
			alphabet_set.append(letter)

	combination = itertools.product(alphabet_set, repeat = n)
	for c in combination:
		str1 = ''.join(c)
		lexicographical_set.append(str1)
	return (lexicographical_set)

def count_mth_k_mer(composition_set, lexicographical_set):
	count = [0]*len(lexicographical_set)
	for inner in range(len(lexicographical_set)):
		for outer in range(len(composition_set)):
			if (lexicographical_set[inner] == composition_set[outer]):
				count[inner] += 1
	return (count)

file = open("rosalind_kmer.txt", "r")
data = file.read().split(">")
file.close()

for line in data:
    if (len(line) == 0):
        continue
    
    parts = line.split()
    string = ''.join(parts[1:])

composition_set = mer_composition(string)
lexicographical_set = lexicographical_composition()
count = count_mth_k_mer(composition_set, lexicographical_set)
for number in count:
	print (number, end=" ")
print()