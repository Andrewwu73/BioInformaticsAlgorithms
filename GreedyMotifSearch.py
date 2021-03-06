#Use a greedy algorithm to search for the best motif.
bestmotifs = []
length, num = map(int, input("").split(" "))
dna = []
# append all the dna strings
for k in range(num):
    dna.append(input(""))
#start with bestmotifs as the set of all motifs.
for m in dna:
    bestmotifs.append(m[0:length])
#We score motifs against consensus string formed from scores.
def scoreMotifs(scores):
    consensus = ""
    count = 0
    for l in range(len(scores[0])):
        tempString= ""
        for a in scores:
            tempString = tempString + a[l]
        a = tempString.count("A")
        c = tempString.count("C")
        g = tempString.count("G")
        t = tempString.count("T")
        y = max(a, c, g, t)
        if(y==a):
            consensus = consensus + "A"
        elif(y==c):
            consensus = consensus + "C"
        elif(y==g):
            consensus = consensus + "G"
        elif(y==t):
            consensus = consensus + "T"
    for m in range(len(scores[0])):
        for xd in scores:
            if(xd[m]!=consensus[m]):
                count = count + 1
            
    return count
#generate motif profile               
for j in range(len(dna[0])-length+1):
    motifList= [dna[0][j:j+length]]
    
    for y in range(1, num):
        profile = [[], [], [], []]
        for itera in range(length):
            profile[0].append(0)
            profile[1].append(0)
            profile[2].append(0)
            profile[3].append(0)
        for motif in motifList:
            for l in range(length):
                if(motif[l]=="A"):
                    profile[0][l] = profile[0][l]+1
                elif(motif[l]=="C"):
                    profile[1][l]=profile[1][l] + 1
                elif(motif[l]=="G"):
                    profile[2][l] = profile[2][l] + 1
                elif(motif[l]=="T"):
                    profile[3][l] = profile[3][l] + 1
        newMotif = ""
        mostProb = -1
        for move in range(len(dna[y])-length+1):
            currentProb = 1
            for stop in range(length):
                if(dna[y][move+stop]=="A"):
                    currentProb = currentProb*profile[0][stop]
                elif(dna[y][move+stop]=="C"):
                    currentProb = currentProb*profile[1][stop]
                elif(dna[y][move+stop]=="G"):
                    currentProb = currentProb*profile[2][stop]
                elif(dna[y][move+stop]=="T"):
                    currentProb = currentProb * profile[3][stop]
            if(currentProb>mostProb):
                mostProb = currentProb
                newMotif = dna[y][move:move+length]
        motifList.append(newMotif)
    if(scoreMotifs(motifList)<scoreMotifs(bestmotifs)):
        bestmotifs = motifList
for m in bestmotifs:
    print(m)