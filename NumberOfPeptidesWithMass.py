numEach = []
massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "L":113, "N":114, "D":115, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
a = int(input(""))
for m in range(a+1):
    numEach.append(0)
numEach[0] = 1
for xd in range(a+1):
    nextNum = numEach[xd]
    for y in massMap:
        if(xd-massMap[y]>=0):
            nextNum = nextNum + numEach[xd-massMap[y]]
    numEach[xd] = nextNum
print(numEach[a])