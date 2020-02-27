#Given a spectrum, find the peptide matching it.
haha = input("").split(" ")
a = []
for m in haha:
    a.append(int(m))
#The maximum peak in the mass spec will be the mass of the actual peptide.
mass =max(a)
#inputting a peptide (a), returns the spectrum of masses associated with it.
def generateCycle(a):
    massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
    stringLists = ['', a]

    for k in range(1,len(a)):
        tempString = a + a[0:k]
        for m in range(len(a)):
            stringLists.append(tempString[m:m+k])

    answers = []
    
    for g in stringLists:
        num = 0
        for xd in g:
            num = num + massMap[xd]
        answers.append(num)
    answers.sort()
    return answers
#generate a spectrum for the linear peptide, useful for checking consistency.
def generateLinear(a):
    massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
    stringLists = ['', a]

    for k in range(1,len(a)):
        tempString = a
        for m in range(len(a)):
            stringLists.append(tempString[m:m+k])

    answers = []
    for g in stringLists:
        num = 0
        for xd in g:
            num = num + massMap[xd]
        answers.append(num)
    answers.sort()
    return answers
#compute mass of a peptide
def massPeptide(pep):
    massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
    ans = 0
    for lol in pep:
        ans = ans + massMap[lol]
    return ans
#check spectrums for equivalence in O(nlogn)
def checkSpectrums(a, b):
    k1 = a
    k2 = b
    k1.sort()
    k2.sort()
    ans = True
    if(len(a)==len(b)):
        for j in range(len(a)):
            if(k1[j]!=k2[j]):
                ans = False
    else:
        ans = False
    return ans
#check consistency, i.e., that the small spectrum is a subset of big.
def checkConsistent(small, big):
    ans = True
    for k in small:
        if(k not in big):
            ans = False
    return ans
peptides = [""]
win = []
massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "N":114, "D":115, "K":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}

while(len(peptides)>0):
    addList = []
    removeList = []
    for m in peptides:
        for y in massMap:
            addList.append(m+y)
        removeList.append(m)
    
    for j in addList:
        peptides.append(j)
    for l in peptides:
        if(massPeptide(l)==mass):
            if(checkSpectrums(generateCycle(l), a)):
                win.append(l)
            removeList.append(l)
        elif(checkConsistent(generateLinear(l), a)==False):
            removeList.append(l)
    for he in removeList:
        peptides.remove(he)
answer = ""
for j in win:
    temp = ""
    for ok in j:
        temp = temp + str(massMap[ok]) + "-"
    answer = answer + temp[0:len(temp)-1] + " "
print(answer)