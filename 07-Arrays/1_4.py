

###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements: ', len(arr))
print('First value:', arr[0])
print('Second value:', arr[1])
print('last value: ', arr[-1])
print('Last value: ', arr[len(arr)-1])
print('sum of the first and last value: ',arr[0]+arr[-1])
print('middle value:',arr[len(arr)//2])
wys=''
for liczba in arr:
    wys+=str(liczba)+','

print('all arrwy values seperated by a single space: ',wys[:-1])
