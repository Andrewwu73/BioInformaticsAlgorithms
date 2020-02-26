a = "temp"
file = open('answer.txt', 'w')
strings =[]
#Continue to take inputted kmers until an empty line is entered.
while a!="":
    a = input("")
    if(len(a)>0):
        strings.append(a)
#Build the overlap graph mapping each element whose prefix equals the suffix of another string to have an edge.
connectDict = {}
k = len(strings[0])
for m in strings:
    for n in strings:
        if(m[0:k-1]==n[1:k]):
            connectDict[n] = m
#Format and save the adjacency list.
for l in connectDict:
    file.write(l + " -> " + connectDict[l]+ "\n")
file.close()