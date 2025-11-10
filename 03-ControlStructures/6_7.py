

wiek=int(input('wpisz swoj wiek: '))
if wiek>=65:
    osoba='Senior'
elif wiek>=20:
    osoba='Adult'
elif wiek>=13:
    osoba='Teen'
else:
    osoba='Child'


print(f'jesteś {osoba}')