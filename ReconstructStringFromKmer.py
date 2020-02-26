kmers = []
lenerBoi = int(input(""))
a = "nice"
while len(a)>1:
    a = input("")
    if(len(a)>1):
        kmers.append(a)
graph = {}
for m in kmers:
    prefix = m[0:len(m)-1]
    suffix = m[1:len(m)]
    if(prefix in graph):
        graph[prefix] = graph[prefix]+[suffix]
    else:
        graph[prefix] = [suffix]


import random

toAdd = []
for unlucky in graph:
    for m in graph[unlucky]:
        if(m not in graph):
            toAdd.append(m)
for l in toAdd:
    graph[l] = []
oddDegree = []
degreeDictionary = {}
for m in graph:
    if(m not in degreeDictionary):
        degreeDictionary[m] = len(graph[m])
    else:
        degreeDictionary[m] = degreeDictionary[m]+len(graph[m])
    for j in graph[m]:
        if(j not in degreeDictionary):
            degreeDictionary[j] = 1
        else:
            degreeDictionary[j] = degreeDictionary[j]+1
for l in degreeDictionary:
    if(degreeDictionary[l]%2==1):
        oddDegree.append(l)
x = random.randint(0,1)
current = oddDegree[x]
if(len(graph[current])==0):
    current = oddDegree[(x-1)%2]
answer = []
path = [current]
startPossible = []
while(len(graph[current])>0):
    chooseNext = random.randint(1, len(graph[current]))-1
    path.append(graph[current][chooseNext])
    answer.append((current, graph[current][chooseNext]))
    
    current = graph[current].pop(chooseNext)
    
def checkExplored(graph):
    for m in graph:
        if(len(graph[m])>0):
            return False
    return True
for xd in path:
    if(len(graph[xd])>0):
        startPossible.append(xd)
while(not checkExplored(graph)):
    newCurrent = startPossible[random.randint(0, len(startPossible)-1)]
    temp = newCurrent
    cycle = []
    cycleNodes = [newCurrent]
    
    while(len(graph[newCurrent])>0):
        chooseNext = random.randint(1, len(graph[newCurrent]))-1
        cycle.append((newCurrent, graph[newCurrent][chooseNext]))
        if(len(graph[newCurrent])==1 and newCurrent in startPossible):
            startPossible.remove(newCurrent)
        if(graph[newCurrent][chooseNext] not in path):
            path.append(graph[newCurrent][chooseNext])
        newCurrent = graph[newCurrent].pop(chooseNext)
        cycleNodes.append(newCurrent)
    done = False
    for l in range(len(answer)):
        if(answer[l][0]==temp and done == False):
            for m in range(len(cycle)):
                answer.insert(l+m, cycle[m])
            done = True
        elif(answer[l][1]==temp and done == False):
            for m in range(len(cycle)):
                answer.insert(l+m+1, cycle[m])
            done = True
    for xd in path:
        if(len(graph[xd])>0 and (xd not in startPossible)):
            startPossible.append(xd)
ans = answer[0][0]
for m in range(len(answer)):
    ans = ans + answer[m][1][lenerBoi-2]

f = open('reconstructString.txt', 'w')
f.write(ans)
f.close()