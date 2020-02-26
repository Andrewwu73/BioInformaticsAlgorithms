a = input("")
b = int(input(""))
matrix = []
for m in range(4):
    matrix.append(input().split(" "))
maxString = ""
maxNum = -1
for val in range(len(a)-b):
    num = 1
    for k in range(b):
        if(a[val+k]=="A"):
            num = num * float(matrix[0][k])
        elif(a[val+k]=="C"):
            num = num * float(matrix[1][k])
        elif(a[val+k]=="G"):
            num = num * float(matrix[2][k])
        elif(a[val+k]=="T"):
            num=num*float(matrix[3][k])
    if(num>maxNum):
        maxNum = num
        maxString = a[val:val+b]
print(maxString)