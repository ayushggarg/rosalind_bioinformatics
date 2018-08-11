def gc(base):
	count = 0
	for letter in base:
		if (letter == 'C' or letter == 'G'):
			count += 1
	return ((count/len(base))*100)

file = open("rosalind_gc.txt", "r")
data = file.read().split(">")
file.close()

max_gc_label = ""
max_gc_base = 0

for line in data:
	if len(line) == 0:
		continue

	parts = line.split()
	label = parts[0]
	base = ''.join(parts[1:])

	gc_content = gc(base)

	if (gc_content > max_gc_base):
		max_gc_label = label
		max_gc_base = gc_content

print (max_gc_label)
print (max_gc_base)



