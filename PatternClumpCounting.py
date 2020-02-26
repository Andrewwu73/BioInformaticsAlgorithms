a = input("")
b, c, d = map(int, input("").split(" "))
answer = []
for m in range(len(a)-c):
    dictionary = {}
    for l in range(c-b):
        if(a[l+m:l+m+b] in dictionary):
            dictionary[a[l+m:l+m+b]] = dictionary[a[l+m:l+m+b]] + 1
        else:
            dictionary[a[l+m:l+m+b]] = 1
        
    for l in dictionary:
        if(dictionary[l]>=d):
            answer.append(l)
answer = list(set(answer))
xd = ""
for m in answer:
    xd = xd + m + " "
print(xd)