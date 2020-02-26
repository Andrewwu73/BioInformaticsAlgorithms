a = input("")
b, d = map(int, input("").split(" "))
dictionary = {}
def flip(a):
    if(a=="A"):
        return "T"
    if(a=="T"):
        return "A"
    if(a=="C"):
        return "G"
    if(a=="G"):
        return "C"
ans = ""
for lul in a:
    ans = ans + flip(lul)
nxtString = ans[::-1]

def countMismatch(a, b):
    count = 0
    for l in range(len(a)):
        if(a[l]!=b[l]):
            count = count + 1
    return count
for k in range(len(a)-b+1):
    testString = a[k:k+b]
        
    addList = [testString]
    for x in range(d):
        addQueue = []
        for lol in addList:
            for l in range(len(lol)):
                addQueue.append(lol[0:l] + "A"+ lol[l+1:len(testString)])
                addQueue.append(lol[0:l] + "T"+ lol[l+1:len(testString)])
                addQueue.append(lol[0:l] + "C"+ lol[l+1:len(testString)])
                addQueue.append(lol[0:l] + "G"+ lol[l+1:len(testString)])
        for each in addQueue:
             addList.append(each)
    for m in dictionary:
        if(countMismatch(m, a[k:k+b])<=d):
            dictionary[m] = dictionary[m] + 1
    for xd in addList:
        if(xd not in dictionary):
            dictionary[xd] = 1
for k in range(len(nxtString)-b+1):
    testString = nxtString[k:k+b]
        
    addList = [testString]
    for x in range(d):
        addQueue = []
        for lol in addList:
            for l in range(len(lol)):
                addQueue.append(lol[0:l] + "A"+ lol[l+1:len(testString)])
                addQueue.append(lol[0:l] + "T"+ lol[l+1:len(testString)])
                addQueue.append(lol[0:l] + "C"+ lol[l+1:len(testString)])
                addQueue.append(lol[0:l] + "G"+ lol[l+1:len(testString)])
        for each in addQueue:
             addList.append(each)
    for m in dictionary:
        if(countMismatch(m, nxtString[k:k+b])<=d):
            dictionary[m] = dictionary[m] + 1
    for xd in addList:
        if(xd not in dictionary):
            dictionary[xd] = 1
maxNum =1
answerList = []
for val in list(dictionary):
    if(dictionary[val]>maxNum):
        answerList = []
        answerList.append(val)
        maxNum = dictionary[val]
    elif(dictionary[val]==maxNum):
        answerList.append(val)
ansString= ""
for m in answerList:
    ansString = ansString + m + " "
print(ansString)