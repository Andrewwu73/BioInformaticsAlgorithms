a = input("")
b = input("")
lengths = []

for x in range(len(a)+1):
    temp = []
    for y in range(len(b)+1):
        temp.append((0, ""))
    lengths.append(temp)
for x in range(len(a)+1):
    for y in range(len(b)+1):
        if(x>0 and y>0):
            d = lengths[x][y-1][0]+1
            e =lengths[x-1][y][0]+1
            f = lengths[x-1][y-1][0]
            if(a[x-1]!=b[y-1]):
                f = f + 1
            troll = min(d, e, f)
            if(troll ==d):
                lengths[x][y] = (troll, "Y")
            elif(troll==e):
                lengths[x][y] = (troll, "X")
            elif(troll == f):
                lengths[x][y] = (troll, "D")
            
        elif(x>0):
            lengths[x][y] = (lengths[x-1][y][0]+1, "X")
        elif(y>0):
            lengths[x][y] = (lengths[x][y-1][0]+1, "Y")

aPath = []
bPath = []
currentCell = (len(a), len(b))
while(currentCell!=(0, 0)):
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

ans = 0
for m in range(len(aPath)):
    if(aPath[m]!=bPath[m]):
        ans = ans + 1
print(ans)