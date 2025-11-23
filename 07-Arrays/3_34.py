def identity_matrix(n):
    macierz=[]
    for i in range(n):
        lista=[]
        for j in range(n):
            if j!=i:
                lista.append(0)
            else:
                lista.append(1)
        macierz.append(lista)
    return macierz

lista=identity_matrix(8)
for wiersz in lista:
    print(" ".join(map(str,wiersz)))
