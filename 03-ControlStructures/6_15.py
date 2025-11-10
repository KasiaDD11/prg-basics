

ean=str(input('wpisz numer EAN-13: '))
if len(ean)==13:
    print('Article number is correct')
    if ean[:3]=='590':
        print('Article manufactured in Poland')