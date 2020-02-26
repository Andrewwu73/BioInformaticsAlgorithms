a = input("")
b = int(input(""))
dictionary = {}
for k in range(len(a)-b+1):
    if(a[k:k+b] in dictionary):
        dictionary[a[k:k+b]] = dictionary[a[k:k+b]]+1
    else:
        dictionary[a[k:k+b]] = 1
maxNum =1
answerList = []
for val in list(dictionary):
    if(dictionary[val]>maxNum):
        answerList = []
        answerList.append(val)
        maxNum = dictionary[val]
    elif(dictionary[val]==maxNum):
        answerList.append(val)
ansString= ""
for m in answerList:
    ansString = ansString + m + " "
print(ansString)