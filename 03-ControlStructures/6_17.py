
godzina=str(input('wpisz godine(HH:mm): '))

if int(godzina[:2])>12:
    nowa_godzina=str(int(godzina[:2])-12)+godzina[2:]+'.pm'
    print(nowa_godzina)
else:
    print(godzina+'.am')



