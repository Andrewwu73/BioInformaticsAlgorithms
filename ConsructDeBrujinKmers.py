kmers = []
file = open('deBrujinFromKmer.txt', 'w')
a = "temp"
#Continue to take input(kmers) until they enter a space.
while len(a)>0:
    a = input("")
    if(len(a)>0):
        kmers.append(a)
dictionary = {}
#Construct the De Brujin graph as an adjacency list.
for m in kmers:
    prefix = m[0:len(m)-1]
    suffix = m[1:len(m)]
    if(prefix in dictionary):
        dictionary[prefix] = dictionary[prefix]+","+suffix
    else:
        dictionary[prefix] = suffix
for xd in dictionary:
    file.write(xd+" -> " +dictionary[xd]+'\n')

file.close()