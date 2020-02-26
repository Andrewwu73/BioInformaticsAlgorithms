codeMap = {"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CGU":"R", "CGC":"R", "CGA":"R", "CGG": "R", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GCU": "A", "GCC":"A", "GCA":"A", "GCG":"A", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "UUG":"L", "UUA":"L", "UUC":"F", "UUU":"F", "UGG":"W", "UGA":"*", "UGC":"C", "UGU":"C", "UCG":"S", "UCA":"S", "UCC":"S", "UCU":"S", "UAG":"*", "UAA":"*", "UAC":"Y", "UAU":"Y"}
a = input("")
ansString = ""
for k in range(int(len(a)/3)):
    if codeMap[a[3*k:3*k+3]]=="*":
        break
    else:
        ansString = ansString + codeMap[a[3*k:3*k+3]]
print(ansString)