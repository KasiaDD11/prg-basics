x=int(input('wpisz x: '))
y=int(input('wpisz y: '))
if x>0 and y>0:
    print ('Jesteś w ćwiartce I')
elif x>0 and y<0:
    print('Jesteś w ćwiartce IV')
elif x<0 and y>0:
    print('Jesteś w ćwiartce II')
elif x<0 and y<0:
    print('Jesteś w ćwiartce III')
else:
    print('Jesteś na osi OX lub OY')
