matrix=[
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j:
            matrix[i][j]=1
        
for wiersz in matrix:
    print(' '.join(map(str,wiersz)))