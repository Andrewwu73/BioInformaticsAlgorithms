#Take in M = cap, the maximum amount of elements in the convolution spectrum to consider, N = the max amount of elements in the leaderboard,
#And a = the actual spectrum
cap = int(input(""))
n = int(input(""))
a = input("").split(" ")
#Construct the spectrum from the input list a.
spectrum = []
for l in a:
    spectrum.append(int(l))
#Construct the convolution dictionary, mapping a convolution difference to its number of occurences.
dictionary = {}
for m in spectrum:
    for y in spectrum:
        if(m!=y):
            if(abs(m-y) in dictionary):
                dictionary[abs(m-y)]= dictionary[abs(m-y)]+1
            else:
                dictionary[abs(m-y)] = 1
#initialize dictionary
aminosPossible = []
totalCount = 0
massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
#Only considering fragments with mass between 57 and 200.
#We find the top m fragments in the fragment dictionary.
while(totalCount<cap and len(dictionary)>0):
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
#Total count gives the total number of mass fragment counts we are considering
#We implement a scoring function to compare a candidate peptide a, and sequence b.
#The peptide sequence a is always passed as a list of values, rather than letters, so we don't need to map to masses.
def score(a, b):
    #massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
    stringLists = ['', a]
    #We construct tempString, an "elongated" a, so that we can account for the peptide being cyclic.
    for k in range(1,len(a)):
        tempString = a + a[0:k]
        for m in range(len(a)):
            stringLists.append(tempString[m:m+k])
    aDict = {}
    #For each possible fragment sequence, we construct the spectrum
    for g in stringLists:
        num = 0
        for val in g:
            num = num + val
        if(num not in aDict):
            aDict[num] = 1
        else:
            aDict[num] = aDict[num] + 1
    #Format the spectrum to a dictionary for comparison
    bDict = {}
    for k in b:
        if(k not in bDict):
            bDict[k] = 1
        else:
            bDict[k] = bDict[k] + 1
    score = 0
    #Use the standard scoring function; if the spectrummatches, add equal to the "extent" of matching.
    for k in aDict:
        if(k in bDict):
            score = score + min(bDict[k], aDict[k])

    return score
#We cut the leaderboard size down to only the top N performers based on the spectrum
def cut(leaderBoard, spectrum, N):
    newBoard = []
    newScores = []
    #For each element, we score it and see if we can add it to the newboard.
    for k in leaderBoard:
        kt = score(k, spectrum)
        if(len(newBoard)==0):
            newBoard.append(k)
            newScores.append(kt)
        elif(len(newBoard)<N):
            found = False
            #Find new location to insert
            for m in range(len(newScores)):
                if(kt>newScores[m] and found == False):
                    found = True
                    newScores.insert(m, kt)
                    newBoard.insert(m, k)
            if(found==False):
                newScores.append(kt)
                newBoard.append(k)
        elif(kt==min(newScores)):
            #If it is the current min, add it to the end
            newBoard.append(k)
            newScores.append(kt)
        elif(kt>min(newScores)):
            #If the board is full and this is a new one that is bigger, we insert it in the middle.
            found = False
            for m in range(len(newScores)):
                if(kt>newScores[m] and found == False):
                    found = True
                    newScores.insert(m, kt)
                    newBoard.insert(m, k)
    #Only return the top N, but now we have to fix the board 
    actualReturned = newBoard[0:N]
    #If there are elements equal to the smallest one in score, we add them to consider.
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
#Helper function to compute the mass of a peptide string
#We pass the amino sequences by mass anyways, so we don't need the mass map
def massPeptide(string):
    #massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
    ans = 0
    for lol in string:
        ans = ans + lol
    return ans
#Continue to build and update the leaderboard until we have a leaderpeptide.
while len(leaderBoard)>0:
    addList = []
    removeList = []
    #continue to add amino acids possible to the growing peptide chains, removing the old ones that are not good.
    for m in leaderBoard:
        for y in aminosPossible:
            addList.append(m+[y])
        removeList.append(m)
    for j in addList:
        leaderBoard.append(j)
    for peptide in leaderBoard:
        
        temp=massPeptide(peptide)
        if(temp==mass):
            if(score(peptide, spectrum)>score(leaderPeptide, spectrum)):
                leaderPeptide = peptide
                removeList.append(peptide)
        elif(temp>mass):         
            removeList.append(peptide)
    for he in removeList:
        leaderBoard.remove(he)
    
    leaderBoard = cut(leaderBoard, spectrum, n)
answer = ""
for k in leaderPeptide:
    answer = answer + str(k)+ "-"
print(answer[0:len(answer)-1])