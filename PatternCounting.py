a = input("")
b = input("")
count = 0
for k in range(len(a)-len(b)+1):
    if(a[k:k+len(b)]==b):
        count = count + 1
print(count)