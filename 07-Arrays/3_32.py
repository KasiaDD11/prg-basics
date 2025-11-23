lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
for wiersz in lista:
    print(" ".join(map(str,wiersz)))

def swap(arr):
    pomoc=arr[0]
    arr[0]=arr[-1]
    arr[-1]=pomoc

swap(lista)
for wiersz in lista:
    print(" ".join(map(str,wiersz)))