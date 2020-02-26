a = int(input(""))
dna = []
while True:
    dn = input()
    if dn:
        dna.append(dn)
    else:
        break
def countMismatch(a, b):
    count = 0
    for le in range(len(a)):
        if(a[le]!=b[le]):
            count = count + 1
    return count
apatterns = ["A", "T", "C", "G"]
patterns = []
for m in range(a-1):
    addQueue = []
    for lol in apatterns:
        addQueue.append(lol+"A")
        addQueue.append(lol+"T")
        addQueue.append(lol+"C")
        addQueue.append(lol+"G")
    for each in addQueue:
        apatterns.append(each)
        if(len(each)==a):
            patterns.append(each)
    
dictionary = {}
for sad in patterns:
    sumDistance = 0
    for lul in dna:
        minDistance = 9999999
        for wee in range(len(lul)-a):
            x = countMismatch(lul[wee:wee+a], sad)
            if(x<minDistance):
                minDistance = x
        sumDistance = sumDistance + minDistance
    dictionary[sad] = sumDistance
minimum = 999999
ans = ""
for l in dictionary:
    if(dictionary[l]<minimum):
        minimum = dictionary[l]
        ans = l
print(ans)