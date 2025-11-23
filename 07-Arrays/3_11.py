def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]> arr[j+1]:
                pomoc=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=pomoc
    return arr
print(bubble_sort([1,9,3,6,2,3,1]))
print(bubble_sort([5,7,3,9,10,16,3]))
print(bubble_sort([9,8,7,6,5,4,3,2,1]))