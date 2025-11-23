lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
for wiersz in lista:
    print(" ".join(map(str,wiersz)))

def swap(arr):
    for wiersz in lista:
        pomoc=wiersz[0]
        wiersz[0]=wiersz[2]
        wiersz[2]=pomoc


swap(lista)
print(" ")
for wiersz in lista:
    print(" ".join(map(str,wiersz)))