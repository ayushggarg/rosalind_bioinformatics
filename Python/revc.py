file = open("rosalind_revc.txt", "r")
data = file.read()
file.close()

#data = "AAAACCCGGT"
data = data[::-1]
data_ans = ""

for letter in data:
	if letter == "A":
		data_ans += "T"
	elif letter == 'T':
		data_ans += "A"
	elif letter == 'G':
		data_ans += "C"
	elif letter == 'C':
		data_ans += "G"

print (data_ans)