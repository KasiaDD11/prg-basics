
import re
name='files.txt'
plik=open(name,'r')
dane=[]
for linia in plik:
    dane.append(linia.strip())
patern='.*\.[a-z]{4}'
plik.close()
for linia in dane:
    if re.match(patern,linia):
        print(linia)