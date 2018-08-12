import math

def permutation(numbers):
	if (len(numbers) == 0):
		return []
	elif(len(numbers) == 1):
		return [numbers]
	else:
		perm = []
		for i in range(len(numbers)):
			frst = numbers[i]
			remList = numbers[:i] + numbers[i+1:]

			for p in permutation(remList):
				perm.append([frst] + p)
	return perm



n = 7
numbers = []

for i in range(1,n+1):
	numbers.append(i)
#print (numbers)

print (math.factorial(n))
for p in permutation(numbers):
	str1 = ' '.join(str(e) for e in p)
	print (str1)