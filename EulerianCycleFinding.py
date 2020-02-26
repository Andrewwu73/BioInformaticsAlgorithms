#We find the eulerian cycle by randomly traversing the graph. (we assume its existence)
#We do this by randomly traversing and finding cycles. If we find a cycle, we append it to a growing cycle and find a new node on the cycle
#with unvisited edges, and then continue to traverse.
graph = {}
a = "nice"
import random
#Take input in and build the graph
while len(a)>1:
    a = input("").split(" ")
    if(len(a)>1):
        graph[a[0]] = a[2].split(",")
        
#Compute the number of unvisited edges (not removed) in the graph.
def checkExplored(graph):
    total = 0
    for m in graph:
        total = total + len(graph[m])
    return total
#Simply arbitrarily choose to start traversing at the first node in our graph
current = list(graph)[0]
answer = []
cycleNodes = [current]
#Our cycle will start at current (can change!)
#We start with an arbitrary traversal of the graph until there are no further nodes to traverse. It is clear by graph theory that
#This must be a cycle and we end up at current node (if we end up at another node, then there cannot be a cycle in the first place)

while(len(graph[current])>0):
    chooseNext = random.randint(1, len(graph[current]))-1
    answer.append((current, graph[current][chooseNext]))
    temp = graph[current][chooseNext]
    
    graph[current].pop(chooseNext)
    current = temp
    cycleNodes.append(current)
#Now we loop to build the cycle continuously. As long as there are unexplored edges in the graph, we continue to traverse and
#build our graph.Note that it is key we reformat to take in these extra cycles, otherwise our list of nodes no longer forms a large cycle.
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
    #Build new answer, then traverse new cycle/
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