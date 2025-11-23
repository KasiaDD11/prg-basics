arr=[8,2,5,1,9]
arr2=[]
for liczba in arr:
    arr2.append(liczba**2)

print(f'Array: {" ".join(map(str,arr))}')
print(f'2nd power: {" ".join(map(str,arr2))}')