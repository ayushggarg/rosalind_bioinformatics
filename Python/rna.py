file = open("rosalind_rna.txt", "r")
data = file.read()
file.close()

#data = "GATGGAACTTGACTACGTAAATT"

data = data.replace("T", "U")
print (data)