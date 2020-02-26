massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}

a = input("")
b = input("").split(" ")
answers = [0]
for j in range(len(a)):
    for m in range(len(a)-j):
        temp = a[m:m+j+1]
        ans = 0
        for troll in temp:
            ans = ans + massMap[troll]
        answers.append(ans)
answers.sort()
count= 0
for m in answers:
    if(str(m) in b):
        count = count + 1
        b.remove(str(m))
print(count)