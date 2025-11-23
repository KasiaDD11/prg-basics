arr=[2,3,2,5,8,1,9,8]
unique=[]
for liczba in arr:
    if arr.count(liczba)==1:
        unique.append(liczba)

print(f'Array: {" ".join(map(str,arr))}')
print(f'Unique elements: {" ".join(map(str,unique))}')