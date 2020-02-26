a = input("").split(" ")
spectrum = []
for l in a:
    spectrum.append(int(l))

dictionary = {}
for m in spectrum:
    for y in spectrum:
        if(m!=y):
            if(abs(m-y) in dictionary):
                dictionary[abs(m-y)]= dictionary[abs(m-y)]+1
            else:
                dictionary[abs(m-y)] = 1
answer = ""
for k in range(len(dictionary)):
    maxCount = -1
    maxString = 0
    for y in dictionary:
        if(dictionary[y]>maxCount):
            maxCount = dictionary[y]
            maxString = y
    count = int((dictionary.pop(maxString))/2)
    for haha in range(count):
        answer = answer + str(maxString)+ " "
f = open("answer.txt", 'w')
f.write(answer[0:len(answer)-1])
f.close()