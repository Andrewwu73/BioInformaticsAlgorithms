b = input("")
a = input("")
ansList = []
#Iterate over string a. If there is a substring equal to b, just add it to the list and return it.
for k in range(len(a)-len(b)+1):
    if(a[k:k+len(b)]==b):
        ansList.append(k)
answer = ""
for j in ansList:
    answer = answer + str(j) + " "
print(answer)