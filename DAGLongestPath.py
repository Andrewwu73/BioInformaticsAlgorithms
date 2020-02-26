import math
#Find the longest edge using DAG relaxation.
a = int(input(""))
b = int(input("")) 
edge ="temp"
lengths= []
edges = []
maxEdgeNum = b
inp = []
#This loop takes in all the input edges, and also determines the maxEdgeNum, the value of the largest vertex(all vertices are assumed
# to be numbered from 0-> maxEdgeNum)
while(len(edge)>1):
    edge = input("").split("->")
    
    if(len(edge)>1):
        inp.append(edge)
        temp = edge[1].split(":")
        if(int(temp[0])>maxEdgeNum):
            maxEdgeNum = int(temp[0])
        if(int(edge[0])>maxEdgeNum):
            maxEdgeNum = int(edge[0])
#Build the edges graph
for m in range(maxEdgeNum+1):
    lengths.append(0)
    temp = []
    for l in range(maxEdgeNum+1):
        temp.append(0)
    edges.append(temp)
#Assign each edge its weight.
for go in inp:
    temp = go[1].split(":")
    edges[int(go[0])][int(temp[0])] = int(temp[1])
#Maintain a list of visited edges.
visited = []
#Returns a stack that is the topological ordering to visit the edges in
def topologicalSortUtil(edges, vertex, visited, stack):
    visited[vertex] = True
    for i in range(len(edges[vertex])):
        if(edges[vertex][i]>0):
            if(visited[i]==False):
                visited, stack = topologicalSortUtil(edges, i, visited, stack)
    stack.insert(0, vertex)
    return visited, stack
#build visited array
for m in range(maxEdgeNum+1):
    visited.append(False)
topologicalStack = []
#Construct topological stack
for i in range(len(visited)):
    if(visited[i]==False):
        visited, topologicalStack = topologicalSortUtil(edges, i, visited, topologicalStack)
values = []
#Max length for each edge
for m in range(0, maxEdgeNum+1):
    values.append((-math.inf, str(m)))
values[a] = (0, str(a))
#Backtrack to build the actual longest path and its length
for m in topologicalStack:
    for l in range(len(edges[m])):
        if(edges[m][l]>0):
            if(values[l][0]<values[m][0]+edges[m][l]):
                values[l]=(values[m][0]+edges[m][l], values[m][1]+"->"+str(l))
print(values[b][0])
print(values[b][1])
#find topological sorting