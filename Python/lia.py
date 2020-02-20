import math

k = 7
n = 36

org_k_level = 2**k
probab_present = 1/4
probab_total_org = 0

for i in range (n, org_k_level+1):
	nCr = math.factorial(org_k_level)/(math.factorial(org_k_level-i)*math.factorial(i))
	probab_total_org += nCr*(probab_present**i)*((1 - probab_present)**(org_k_level-i))
print (probab_total_org)