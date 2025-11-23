def compare(arr1,arr2):
    if len(arr1)!=len(arr2):
        return False
    else:
        for i in range(len(arr1)):
            if arr1[i]!=arr2[i]:
                return False
            
    return True
arr=['water','book','sky']
print(compare(['water','book','sky'],['water','book','sky']))
print(f'Array1: {" ".join(map(str,arr))}')
print(f'Array1: {" ".join(map(str,arr))}')
if compare(['water','book','sky'],['water','book','sky'])==True:
    print('Comparison: arrays are the same')
else:
    print('Comparison: arrays are not the same')

print(compare([True,False],[True,False,True]))
print(compare([5,3,1],[5,6,1]))
print(compare([3,2,1],[3,2]))