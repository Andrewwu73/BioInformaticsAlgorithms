b = input("")
a = input("")
ansList = []
for k in range(len(a)-len(b)+1):
    if(a[k:k+len(b)]==b):
        ansList.append(k)
answer = ""
for j in ansList:
    answer = answer + str(j) + " "
print(answer)