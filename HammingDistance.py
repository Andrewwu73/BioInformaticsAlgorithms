a = input("")
b = input("")
count = 0
for k in range(len(a)):
    if(a[k]!=b[k]):
        count = count + 1
print(count)