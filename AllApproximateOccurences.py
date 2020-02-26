def numDifferences(a, b):
    count = 0
    for k in range(len(a)):
        if(a[k]!=b[k]):
            count = count + 1
    return count

a = input("")
b = input("")
d = int(input(""))
answerList = []
for k in range(len(b)-len(a)):
    if(numDifferences(b[k:k+len(a)], a)<=d):
        answerList.append(k)
ansString = ""
for m in answerList:
    ansString = ansString + str(m)+ " "
print(ansString)