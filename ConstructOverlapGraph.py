a = "XD"
file = open('answer.txt', 'w')
strings =[]
while a!="":
    a = input("")
    if(len(a)>0):
        strings.append(a)

connectDict = {}
k = len(strings[0])
for m in strings:
    for n in strings:
        if(m[0:k-1]==n[1:k]):
            connectDict[n] = m
for l in connectDict:
    file.write(l + " -> " + connectDict[l]+ "\n")
file.close()