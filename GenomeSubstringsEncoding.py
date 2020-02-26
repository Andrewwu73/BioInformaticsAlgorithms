codeMap = {"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CGU":"R", "CGC":"R", "CGA":"R", "CGG": "R", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GCU": "A", "GCC":"A", "GCA":"A", "GCG":"A", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "UUG":"L", "UUA":"L", "UUC":"F", "UUU":"F", "UGG":"W", "UGA":"*", "UGC":"C", "UGU":"C", "UCG":"S", "UCA":"S", "UCC":"S", "UCU":"S", "UAG":"*", "UAA":"*", "UAC":"Y", "UAU":"Y"}
xa = input("")
b = input("")
reverse = ""
def flip(a):
    if(a=="A"):
        return "U"
    if(a=="T"):
        return "A"
    if(a=="C"):
        return "G"
    if(a=="G"):
        return "C"
a = ""
for m in xa:
    if(m=="T"):
        a = a + "U"
    else:
        a = a + m
for lul in xa:
    reverse = flip(lul)+reverse
for m in range(len(a)-3*len(b)):
    test1 = ""
    test2 = ""
    for k in range(len(b)):
        test1 = test1 + codeMap[a[m+3*k:m+3*k+3]]
        test2 = test2 + codeMap[reverse[m+3*k:m+3*k+3]]
    if(test1==b):
        print(xa[m:m+3*len(b)])
    if(test2==b):
        print(xa[len(a)-m-3*len(b):len(a)-m])