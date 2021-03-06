a = input("")
massMap ={"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
stringLists = ['', a]
#Score a cyclic peptide against a spectrum.
#Construct the set of possible peptide fragment strings by cyclicizing the stiring and finding substrings.
for k in range(1,len(a)):
    tempString = a + a[0:k]
    for m in range(len(a)):
        stringLists.append(tempString[m:m+k])

answers = []
ans = ""
#For each possible string, we compute "answers" the set of masses
for g in stringLists:
    num = 0
    for mas in g:
        num = num + massMap[mas]
    answers.append(num)

answers.sort()
#Take in the input s, the spectrum to compare the "answers" to.
s = input("").split(" ")
b = []
for l in s:
    b.append(int(l))
score = 0
done = []
#If there is a fragment in both specturms, then we can increase the score.
for k in answers:
    if(k not in done):
        score = score + min(answers.count(k), b.count(k))
        done.append(k)

print(score)