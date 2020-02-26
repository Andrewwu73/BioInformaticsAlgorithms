a = input("")
b = input("")
lengths = []
#We proceed using DP. Initialize a 2D array, representing solutions to the DP problem X(i, j)
#where the X(i, j) subproblem means we need to compute the distance between the a[:i] substring and b[:j] substring.
for x in range(len(a)+1):
    temp = []
    for y in range(len(b)+1):
        temp.append((0, ""))
    lengths.append(temp)

#Perform DP in O(|A||B|) runtime. In saving backtracking, we use Y to represent a decrease in the Y coordinate (with +1 edit distance),
#X represents the analog in x direction, and D means there is no change, they are equal.
for x in range(len(a)+1):
    for y in range(len(b)+1):
        if(x>0 and y>0):
            d = lengths[x][y-1][0]+1
            e =lengths[x-1][y][0]+1
            f = lengths[x-1][y-1][0]
            if(a[x-1]!=b[y-1]):
                f = f + 1
            temp = min(d, e, f)
            if(temp ==d):
                lengths[x][y] = (temp, "Y")
            elif(temp==e):
                lengths[x][y] = (temp, "X")
            elif(temp == f):
                lengths[x][y] = (temp, "D")
            
        elif(x>0):
            lengths[x][y] = (lengths[x-1][y][0]+1, "X")
        elif(y>0):
            lengths[x][y] = (lengths[x][y-1][0]+1, "Y")

#Our lengths DP memoization included the X, Y, D saving to backtrack, so we do it as follows
aPath = []
bPath = []
currentCell = (len(a), len(b))
#Backtrack until we're at the start again.
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
#Finally, format the answer to return.
ans = 0
for m in range(len(aPath)):
    if(aPath[m]!=bPath[m]):
        ans = ans + 1
print(ans)