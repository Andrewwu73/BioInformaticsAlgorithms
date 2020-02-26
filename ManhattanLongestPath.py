m, n = map(int, input("").split(" "))
down = []
for oops in range(m):
    down.append(input("").split(" "))
xd = input("")
right = []
for oopsies in range(m+1):
    right.append(input("").split(" "))
lengths = []
for x in range(m+1):
    temp = []
    for y in range(n+1):
        temp.append(0)
    lengths.append(temp)
for x in range(m+1):
    for y in range(n+1):
        if(x>0 and y>0):
            lengths[x][y] = max((lengths[x][y-1]+int(right[x][y-1])), (lengths[x-1][y]+int(down[x-1][y])))
        elif(x>0):
            lengths[x][y] = lengths[x-1][y]+int(down[x-1][y])
        elif(y>0):
            lengths[x][y] = lengths[x][y-1]+int(right[x][y-1])
print(lengths[m][n])