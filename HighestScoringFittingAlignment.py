a  = input("")
b  = input("")
lengths = []
for x in range(len(a)+1):
    temp = []
    for y in range(len(b)+1):
        temp.append((0, ""))
    lengths.append(temp)
for x in range(len(a)+1):
    for y in range(len(b)+1):
        if(x>0 and y>0):
            d = lengths[x][y-1][0]-1
            e = lengths[x-1][y][0]-1
            f = lengths[x-1][y-1][0]
            if(a[x-1]==b[y-1]):
                f = f + 1
            else:
                f = f - 1
            troll = max(d, e, f)
            if(troll==d):
                lengths[x][y] = (troll, "Y")
            elif(troll==e):
                lengths[x][y] = (troll, "X")
            elif(troll==f):
                lengths[x][y] = (troll, "D")
        
maxVal = -99999999
backStart = 0
for x in range(len(b), len(a)+1):
    if(lengths[x][len(b)][0]>maxVal):
        maxVal = lengths[x][len(b)][0]
        backStart = x
aPath = []
bPath = []
currentCell = (backStart, len(b))
while(currentCell[1]>0 and currentCell[0]>0):
    if(lengths[currentCell[0]][currentCell[1]][1]=="D"):
        aPath.insert(0, a[currentCell[0]-1])
        bPath.insert(0, b[currentCell[1]-1])
        currentCell = (currentCell[0]-1, currentCell[1]-1)
    elif(lengths[currentCell[0]][currentCell[1]][1]=="Y"):
        aPath.insert(0, "-")
        bPath.insert(0, b[currentCell[1]-1])
        currentCell = (currentCell[0], currentCell[1]-1)
    elif(lengths[currentCell[0]][currentCell[1]][1]=="X"):
        aPath.insert(0, a[currentCell[0]-1])
        bPath.insert(0, "-")
        currentCell = (currentCell[0]-1, currentCell[1])
print(maxVal)
print("".join(aPath))
print("".join(bPath))