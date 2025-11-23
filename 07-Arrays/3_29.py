def create_2d_arr(x,y):
    lista=[]

    for i in range(y):
        lis=[]
        
        for j in range(x):
            lis.append(0)
        lista.append(lis)
    return lista

print(create_2d_arr(3,5))
for wiersz in create_2d_arr(3,5):
    print(" ".join(map(str,wiersz)))