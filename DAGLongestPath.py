import math
a = int(input(""))
b = int(input(""))
xd ="yikes"
lengths= []
edges = []
maxEdgeNum = b
inp = []
while(len(xd)>1):
    xd = input("").split("->")
    
    if(len(xd)>1):
        inp.append(xd)
        troll = xd[1].split(":")
        if(int(troll[0])>maxEdgeNum):
            maxEdgeNum = int(troll[0])
        if(int(xd[0])>maxEdgeNum):
            maxEdgeNum = int(xd[0])
for m in range(maxEdgeNum+1):
    lengths.append(0)
    temp = []
    for l in range(maxEdgeNum+1):
        temp.append(0)
    edges.append(temp)
for xd in inp:
    troll = xd[1].split(":")
    edges[int(xd[0])][int(troll[0])] = int(troll[1])
visited = []
def topologicalSortUtil(edges, vertex, visited, stack):
    visited[vertex] = True
    for i in range(len(edges[vertex])):
        if(edges[vertex][i]>0):
            if(visited[i]==False):
                visited, stack = topologicalSortUtil(edges, i, visited, stack)
    stack.insert(0, vertex)
    return visited, stack

for m in range(maxEdgeNum+1):
    visited.append(False)
topologicalStack = []
for i in range(len(visited)):
    if(visited[i]==False):
        visited, topologicalStack = topologicalSortUtil(edges, i, visited, topologicalStack)
values = []
for m in range(0, maxEdgeNum+1):
    values.append((-math.inf, str(m)))
values[a] = (0, str(a))
for m in topologicalStack:
    for l in range(len(edges[m])):
        if(edges[m][l]>0):
            if(values[l][0]<values[m][0]+edges[m][l]):
                values[l]=(values[m][0]+edges[m][l], values[m][1]+"->"+str(l))
print(values[b][0])
print(values[b][1])
#find topological sorting