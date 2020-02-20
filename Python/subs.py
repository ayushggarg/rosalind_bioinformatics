file = open("rosalind_subs.txt", "r")
data = file.read().splitlines()
s = data[0]
t = data[1]
file.close()

#s = "GATATATGCATATACTT"
#t = "ATAT"

s_len = len(s)
t_len = len(t)

for i in range(s_len-t_len+1):
	if (s[i:t_len+i] == t):
		print (i+1, end = " ")
print ()
