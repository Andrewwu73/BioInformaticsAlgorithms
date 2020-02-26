
#Helper function, compute the number of differences between two strings of same length a, b
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
#For each consecutive substring, we compute whether the number of differences is less than d, if it is then it is an approximate occurence.
#This is currently done in O(nk) time; could be done in O(n) by DP-like modification, but this was the intended solution.
for k in range(len(b)-len(a)):
    if(numDifferences(b[k:k+len(a)], a)<=d):
        answerList.append(k)
ansString = ""
for m in answerList:
    ansString = ansString + str(m)+ " "
print(ansString)