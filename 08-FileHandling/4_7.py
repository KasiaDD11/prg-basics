import re
napis=input('wpisz zdanie: ')
wow='[aeiou]'
lista=re.findall(wow,napis)
print(len(lista))