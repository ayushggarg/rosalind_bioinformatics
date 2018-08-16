import math

n = 89
k = 9

perm = 1
for i in range (n-k+1, n+1):
	perm *= i
	perm %= 1000000
print (perm)
