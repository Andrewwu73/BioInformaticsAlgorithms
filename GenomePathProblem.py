a = "xd"
strings = []
while a!="":
	a = input("")
	if(len(a)>0):
		strings.append(a)
answer = strings[0]
xd = len(answer)
for m in range(len(strings)-1):
	answer = answer + strings[m+1][xd-1]
print(answer)