couples = [19252, 17356, 18305, 16158, 17691, 17783]
probability = [1, 1, 1, 0.75, 0.5, 0]
offspring = [0]*6

for i in range(6):
	offspring[i] = 2*couples[i]*probability[i]

print (sum(offspring))