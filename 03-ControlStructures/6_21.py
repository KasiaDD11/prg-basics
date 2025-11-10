cena=int(input('wpisz cene: '))
piec=0
dwa=0
jeden=0


while cena>0:
    if cena>=5:
        piec+=1
        cena=cena-5
    elif cena>=2:
        dwa+=1
        cena=cena-2
    else:
        jeden+=1
        cena=cena-1

print(f'piątek jest: {piec}')
print(f'dwójek jest: {dwa}')
print(f'jedynek jest: {jeden}')
