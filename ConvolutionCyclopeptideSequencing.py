fuk = int(input(""))
n = int(input(""))
a = input("").split(" ")
spectrum = []
for l in a:
    spectrum.append(int(l))

dictionary = {}
for m in spectrum:
    for y in spectrum:
        if(m!=y):
            if(abs(m-y) in dictionary):
                dictionary[abs(m-y)]= dictionary[abs(m-y)]+1
            else:
                dictionary[abs(m-y)] = 1
aminosPossible = []
totalCount = 0
massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
while(totalCount<fuk and len(dictionary)>0):
    maxCount = -1
    maxStrings = []
    amino = ""
    for l in dictionary:
        if(dictionary[l]>maxCount and l>=57 and l<=200):
            maxStrings = [l]
            maxCount = dictionary[l]
        elif(dictionary[l]==maxCount and l>=57 and l<=200):
            maxStrings.append(l)
    for troll in maxStrings:
        aminosPossible.append(troll)
        dictionary.pop(troll)
    totalCount = totalCount + len(maxStrings)
    
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
            num = num + xd
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
            if(found==False):
                newScores.append(kt)
                newBoard.append(k)
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
        
        
                    

mass =max(spectrum)
leaderBoard = [[]]
leaderPeptide = []
def massPeptide(xd):
    massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
    ans = 0
    for lol in xd:
        ans = ans + lol
    return ans
while len(leaderBoard)>0:
    addList = []
    removeList = []
    for m in leaderBoard:
        for y in aminosPossible:
            addList.append(m+[y])
        removeList.append(m)
    for j in addList:
        
        leaderBoard.append(j)
    for peptide in leaderBoard:
        
        hehe=massPeptide(peptide)
        if(hehe==mass):
            if(score(peptide, spectrum)>score(leaderPeptide, spectrum)):
                leaderPeptide = peptide
                removeList.append(peptide)
        elif(hehe>mass):
            
            removeList.append(peptide)
    for he in removeList:
        leaderBoard.remove(he)
    
    leaderBoard = cut(leaderBoard, spectrum, n)
answer = ""
for k in leaderPeptide:
    answer = answer + str(k)+ "-"
print(answer[0:len(answer)-1])