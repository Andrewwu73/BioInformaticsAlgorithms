a = input("")
massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
stringLists = ['', a]
#Compute the cyclic theoretical spectrum from a given peptide a.
for k in range(1,len(a)):
    tempString = a + a[0:k]
    for m in range(len(a)):
        stringLists.append(tempString[m:m+k])

answers = []
ans = ""
#For each possible cyclic fragment, compute its mass and add it to answers.
for g in stringLists:
    num = 0
    for mas in g:
        num = num + massMap[mas]
    answers.append(num)
answers.sort()
for k in answers:
    ans = ans + str(k)+ " "
print(ans[0:len(ans)-1])