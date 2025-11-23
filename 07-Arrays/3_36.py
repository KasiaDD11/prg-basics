def na1d(arr):
    lista=[]
    for wiersz in arr:
        for liczba in wiersz:
            lista.append(liczba)

    return lista


arr1=[[2,3],[1,5]]
arr2=[[5,0,3,7,5],[9,0,9,1,2]]
arr3=[[2,1],[3,5],[7,4],[2,6]]

print(na1d(arr1))
print('----------')
print(na1d(arr2))
print('----------')
print(na1d(arr3))