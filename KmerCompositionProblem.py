a = int(input(""))
b = input("")
ans = []
for m in range(len(b)-a+1):
	ans.append(b[m:m+a])
ans.sort()
for x in ans:
	print(x)