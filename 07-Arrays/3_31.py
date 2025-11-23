lista=[[-38, 19], [5,40],[-7,11],[29,16]]
max=lista[0][0]
max_x=0
max_y=0
min=lista[0][0]
min_x=0
min_y=0

for i in range(len(lista)):
    for j in range(len(lista[i])):
        if lista[i][j]>max:
            max=lista[i][j]
            max_x=i
            max_y=j
        if lista[i][j]<min:
            min=lista[i][j]
            min_x=i
            min_y=j

print(max)
print(max_x)
print(max_y)

print(min)
print(min_x)
print(min_y)