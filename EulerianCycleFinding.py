graph = {}
a = "nice"
import random

while len(a)>1:
    a = input("").split(" ")
    if(len(a)>1):
        graph[a[0]] = a[2].split(",")
        
    
exploredEdges = {}
def checkExplored(graph):
    total = 0
    for m in graph:
        total = total + len(graph[m])
    return total

current = list(graph)[0]
answer = []
cycleNodes = [current]
while(len(graph[current])>0):
    chooseNext = random.randint(1, len(graph[current]))-1
    answer.append((current, graph[current][chooseNext]))
    temp = graph[current][chooseNext]
    
    graph[current].pop(chooseNext)
    current = temp
    cycleNodes.append(current)

while(checkExplored(graph)>0):
    newStart = ""
    for l in cycleNodes:
        if(len(graph[l])>0):
            newStart = l
    
    tempAnswerFront = []
    tempAnswerBack = []
    found = False
    for a in answer:
        if(a[0]==newStart or found == True):
            found = True
            tempAnswerBack.append(a)
        elif(found == False):
            tempAnswerFront.append(a)
    answer = tempAnswerBack + tempAnswerFront
    current = newStart
    
    while(len(graph[current])>0):
        chooseNext = random.randint(1, len(graph[current]))-1
        answer.append((current, graph[current][chooseNext]))
        temp = graph[current][chooseNext]
        graph[current].pop(chooseNext)
        current = temp
        cycleNodes.append(current)
ans = answer[0][0]
for m in range(len(answer)):
    ans = ans + "->"+answer[m][1]
f = open('eulerianCycle.txt', 'w')
f.write(ans)
f.close()