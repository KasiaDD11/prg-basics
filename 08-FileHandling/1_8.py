with open('pets.txt','r') as file:
    plik=[]
    for line in file:
        plik.append(line.split(' '))

sum=0
for linia in plik:
    print(len(linia))
    sum+=len(linia)

print(sum)
    