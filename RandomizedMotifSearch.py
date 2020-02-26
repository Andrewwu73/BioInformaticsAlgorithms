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
bestMotifs = []
length, num = map(int, input("").split(" "))
dna = []
for k in range(num):
    dna.append(input(""))
import random
for holy in range(2000):
    motifs = []
    for m in range(num):
        xd = random.randint(0, len(dna[m])-length)
        motifs.append(dna[m][xd:xd+length])
    if(len(bestMotifs)==0):
        bestMotifs = motifs
    while True:
        profile = [[], [], [], []]
        for xd in range(length):
            profile[0].append(1)
            profile[1].append(1)
            profile[2].append(1)
            profile[3].append(1)
        for motif in motifs:
            for l in range(length):
                if(motif[l]=="A"):
                    profile[0][l] = profile[0][l]+1
                elif(motif[l]=="C"):
                    profile[1][l]=profile[1][l] + 1
                elif(motif[l]=="G"):
                    profile[2][l] = profile[2][l] + 1
                elif(motif[l]=="T"):
                    profile[3][l] = profile[3][l] + 1
        motifs = []
        for j in range(num):
            mostProb = ""
            prob = -1
            for haha in range(len(dna[j])-length+1):
                temp = 1
                for y in range(length):
                    if(dna[j][haha+y]=="A"):
                        temp = temp * profile[0][y]
                    elif(dna[j][haha+y]=="C"):
                        temp = temp * profile[1][y]
                    elif(dna[j][haha+y]=="G"):
                        temp = temp * profile[2][y]
                    elif(dna[j][haha+y]=="T"):
                        temp = temp * profile[3][y]
                if(temp>prob):
                    prob = temp
                    mostProb = dna[j][haha:haha+length]
            motifs.append(mostProb)
        if(scoreMotifs(motifs)<scoreMotifs(bestMotifs)):
            bestMotifs = motifs
        else:
            break
    
for m in bestMotifs:
    print(m)