a = input("")

listXD = []

for m in range(len(a)):
    listXD.append(a[0:m].count("G")-a[0:m].count("C"))

lazy = min(listXD)
ans = ""
for m in range(len(listXD)):
    if(listXD[m]==lazy):
        ans = ans + str(m)+ " "
print(ans)