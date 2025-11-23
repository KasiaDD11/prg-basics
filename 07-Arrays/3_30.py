lista=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
for i in range(1,len(lista)+1):
    for j in range(1,len(lista[i-1])+1):
        lista[i-1][j-1]=i*j


for wiersz in lista:
    print(" ".join(map(str,wiersz)))
print(lista)