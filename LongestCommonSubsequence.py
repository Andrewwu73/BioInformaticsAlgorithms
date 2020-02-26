a = input("")
b = input("")
diagonals = []
for oops in range(len(a)):
    temp = []
    for l in range(len(b)):
        temp.append((0, ""))
    diagonals.append(temp)
for m in range(len(a)):
    for n in range(len(b)):
        if(b[n]==a[m]):
            diagonals[m][n] = (1, a[m])
lengths = []
for x in range(len(a)+1):
    temp = []
    for y in range(len(b)+1):
        temp.append((0, ""))
    lengths.append(temp)
for x in range(len(a)+1):
    for y in range(len(b)+1):
        if(x>0 and y>0):
            sad = max((lengths[x][y-1][0], lengths[x-1][y][0], lengths[x-1][y-1][0]+diagonals[x-1][y-1][0]))
            if(sad==lengths[x][y-1][0]):
                lengths[x][y]= (lengths[x][y-1][0], lengths[x][y-1][1])
            elif(sad==lengths[x-1][y][0]):
                lengths[x][y] = (lengths[x-1][y][0], lengths[x-1][y][1])
            elif(sad==lengths[x-1][y-1][0]+diagonals[x-1][y-1][0]):
                lengths[x][y] = (lengths[x-1][y-1][0]+diagonals[x-1][y-1][0], lengths[x-1][y-1][1]+diagonals[x-1][y-1][1])
        elif(x>0):
            lengths[x][y] = (lengths[x-1][y][0], lengths[x-1][y][1])
        elif(y>0):
            lengths[x][y] = (lengths[x][y-1][0],lengths[x][y-1][1])
print(lengths[len(a)][len(b)][1])