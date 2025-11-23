#Numbers: 7,3,8,5,2
#Second largest number: 7 
#Median: 5
#Smallest and largest number: 2,8
#Numbers as a string: 7-3-8-5-2

def sec_lar(lista):
    lista=sorted(lista)
    return lista

def smal_larg(lista):
    max=lista[0]
    min=lista[0]
    
    for i in range(len(lista)):
        if lista[i]>max:
            max=lista[i]
            
        if lista[i]<min:
            min=lista[i]
            
    wynik=[]
    wynik.append(min)
    wynik.append(max)
    return wynik
def roznica(lista):
    ciag=smal_larg(lista)
    wynik=ciag[1]-ciag[0]
    return wynik
def mediana(lista):
    lista=sec_lar(lista)
    return lista[len(lista)//2]


def as_string(lista):
    wynik=''
    for znak in lista:
        wynik+=str(znak)
        wynik+='-'
    return wynik[:-1]




tup=(7,3,8,5,2)
print(f'Numbers: {tup}')
print(f'Second largest value: {sec_lar(tup)[-2]}')
print(f'Mediana: {mediana(tup)}')
print(f'Smallest and largest values: {smal_larg(tup)}')
print(f'Roznica pomiedzy najwieksza i najmniejsza: {roznica(tup)}')
print(f'Numbers as a string: {as_string(tup)}')
