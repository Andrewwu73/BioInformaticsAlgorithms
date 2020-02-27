a = "xd"
#Given a set of broken genomes, reconstruct the original genome from the common substrings.
strings = []
while a!="":
	a = input("")
	if(len(a)>0):
		strings.append(a)
answer = strings[0]
temp = len(answer)
for m in range(len(strings)-1):
	answer = answer + strings[m+1][temp-1]
print(answer)