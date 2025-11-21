def ciag(liczba):
    ciag="" 
    for i in range(1,liczba+1):
        ciag+=str(i)
    return ciag
print(ciag(11))
print(ciag(4))