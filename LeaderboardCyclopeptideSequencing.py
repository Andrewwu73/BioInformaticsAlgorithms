a = int(input(""))
haha = input("").split(" ")
def score(a, b):
    massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
    stringLists = ['', a]

    for k in range(1,len(a)):
        tempString = a + a[0:k]
        for m in range(len(a)):
            stringLists.append(tempString[m:m+k])

    answers = []
    ans = ""
    aDict = {}
    for g in stringLists:
        num = 0
        for xd in g:
            num = num + massMap[xd]
        if(num not in aDict):
            aDict[num] = 1
        else:
            aDict[num] = aDict[num] + 1
    bDict = {}
    for k in b:
        if(k not in bDict):
            bDict[k] = 1
        else:
            bDict[k] = bDict[k] + 1
    score = 0
    for k in aDict:
        if(k in bDict):
            score = score + min(bDict[k], aDict[k])
    return score
def cut(leaderBoard, spectrum, N):
    newBoard = []
    newScores = []
    
    for k in leaderBoard:
        kt = score(k, spectrum)
        if(len(newBoard)==0):
            newBoard.append(k)
            newScores.append(kt)
        elif(len(newBoard)<N):
            found = False
            for m in range(len(newScores)):
                if(kt>newScores[m] and found == False):
                    found = True
                    newScores.insert(m, kt)
                    newBoard.insert(m, k)
        elif(kt==min(newScores)):
            newBoard.append(k)
            newScores.append(kt)
        elif(kt>min(newScores)):
            found = False
            for m in range(len(newScores)):
                if(kt>newScores[m] and found == False):
                    found = True
                    newScores.insert(m, kt)
                    newBoard.insert(m, k)
    actualReturned = newBoard[0:N]
    
    if(len(newBoard)>=N):
        active = True
        iterate = N
        lastNum = newScores[N-1]
        while active:
            if(iterate>=len(newBoard)):
                active= False
            elif(newScores[iterate]==lastNum):
                actualReturned.append(newBoard[iterate])
                iterate =iterate + 1
            else:
                active = False
    
    return actualReturned
        
        
                    
b = []
for m in haha:
    b.append(int(m))
mass =max(b)
leaderBoard = [""]
leaderPeptide = ""
massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "N":114, "D":115, "K":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
def massPeptide(xd):
    massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
    ans = 0
    for lol in xd:
        ans = ans + massMap[lol]
    return ans
while len(leaderBoard)>0:
    addList = []
    removeList = []
    for m in leaderBoard:
        for y in massMap:
            addList.append(m+y)
        removeList.append(m)
    for j in addList:
        leaderBoard.append(j)
    for peptide in leaderBoard:
        hehe=massPeptide(peptide)
        if(hehe==mass):
            if(score(peptide, b)>score(leaderPeptide, b)):
                leaderPeptide = peptide
                removeList.append(peptide)
        elif(hehe>mass):
            removeList.append(peptide)
    for he in removeList:
        leaderBoard.remove(he)
    
    leaderBoard = cut(leaderBoard, b, a)
answer = ""
for k in leaderPeptide:
    answer = answer + str(massMap[k])+ "-"
print(answer[0:len(answer)-1])