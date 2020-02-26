a = int(input(""))
b = input("")
dictionary = {}
#Construct the De Brujin graph from the string b using the length a kmers.
for m in range(len(b)-a+1):
    if(b[m:m+a-1] not in dictionary):
        dictionary[b[m:m+a-1]] =b[m+1:m+a]
    else:
        dictionary[b[m:m+a-1]]=dictionary[b[m:m+a-1]]+","+b[m+1:m+a]
file = open("deBrujin.txt", "w")
for x in dictionary:
    file.write(x+" -> " +dictionary[x]+ '\n')
file.close()