#.   [1  ,  2]
#.   [3  ,  4]    =>  [1  ,  3  ,  5  ,  7]
#.   [5  ,  6]    =>  [2  ,  4  ,  6  ,  8]
#.   [7  ,  8]

def trans(arr):
    lista2=[]
    for i in range(len(arr[0])):
        pomoc=[]
        for j in range(len(arr)):
            pomoc.append(arr[j][i])
        lista2.append(pomoc)
    return lista2

arr1=[[1,2,3],[4,5,6],[7,8,9]]
arr2=[[1,2,3,4,5],[6,7,8,9,0]]
arr3=[[5,6,7,8]]
arr1=trans(arr1)
arr2=trans(arr2)
arr3=trans(arr3)
for wiersz in arr1:
    print(" ".join(map(str,wiersz)))
print("-----------------")
for wiersz in arr3:
    print(" ".join(map(str,wiersz)))
print("-----------------")
for wiersz in arr2:
    print(" ".join(map(str,wiersz)))

