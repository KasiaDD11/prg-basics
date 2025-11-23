arr = [7,9,2,4,5,6]
arr2=[]
for liczba in arr:
    if liczba%2==0:
        arr2.append(liczba)
for liczba in arr:
    if liczba%2==1:
        arr2.append(liczba)
print(arr2)