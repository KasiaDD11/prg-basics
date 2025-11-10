numer=int(input('Wpisz numer: '))
nowa=''
while numer!=0:
    nowa+=str(numer%2)
    numer=numer//2
print(nowa[::-1])