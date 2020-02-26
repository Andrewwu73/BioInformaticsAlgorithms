a, b = map(int, input("").split(" "))
dna = []
while True:
    dn = input()
    if dn:
        dna.append(dn)
    else:
        break
patterns = []
def countMismatch(a, b):
    count = 0
    for l in range(len(a)):
        if(a[l]!=b[l]):
            count = count + 1
    return count
addList = []
for m in dna:
    for xd in range(len(m)-a):
        addList.append(m[xd:xd+a])
        
for x in range(b):
    addQueue = []
    for lol in addList:
        for l in range(len(lol)):
            addQueue.append(lol[0:l] + "A"+ lol[l+1:len(lol)])
            addQueue.append(lol[0:l] + "T"+ lol[l+1:len(lol)])
            addQueue.append(lol[0:l] + "C"+ lol[l+1:len(lol)])
            addQueue.append(lol[0:l] + "G"+ lol[l+1:len(lol)])
    for each in addQueue:
         addList.append(each)
for pattern in addList:
    ok = True
    for l in dna:
        found = False
        for ined in range(len(l)-a+1):
            if(countMismatch(l[ined:ined+a], pattern)<=b):
                found= True
        
        if(found == False):
            ok = False
    if(ok == True):
        patterns.append(pattern)
patterns = list(set(patterns))
xd = ""
for m in patterns:
    xd = xd + m + " "
print(xd)