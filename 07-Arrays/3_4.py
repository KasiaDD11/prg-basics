arr=[-15,8,-31,47,-2,19]
max=arr[0]
max_id=0
min=arr[0]
min_id=0

for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
        max_id=i
    if arr[i]<min:
        min=arr[i]
        min_id=i


print(max)
print(max_id)
print(min)
print(min_id)