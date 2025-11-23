arr=[15,8,31,47,2,19]
arr2=[]
for i in range(1,len(arr)+1):
    arr2.append(arr[-i])

print(f'existed array: {" ".join(map(str,arr))}')
print(f'reverse array: {" ".join(map(str,arr2))}')