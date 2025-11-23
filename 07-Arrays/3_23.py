tekst='An apple a day keeps the doctor away'

#A function that returns an ordered array of words, from longest to shortest
#A function that returns an alphabetically ordered array of words
def worlds(zdanie):
    return zdanie.count(' ')+1
def slowa(zdanie):
    lista=zdanie.split(' ')
    return sorted(lista,key=len)
def slowa_a(zdanie):
    lista=zdanie.split(' ')
    return sorted(lista)


print(worlds(tekst))
print(slowa(tekst))
print(slowa_a(tekst))