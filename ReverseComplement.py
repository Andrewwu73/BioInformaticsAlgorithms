a = input("")
def flip(a):
    if(a=="A"):
        return "T"
    if(a=="T"):
        return "A"
    if(a=="C"):
        return "G"
    if(a=="G"):
        return "C"
ans = ""
for lul in a:
    ans = ans + flip(lul)
print(ans[::-1])