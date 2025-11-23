def f(tekst):
    nowy=''
    if tekst=='':
        return nowy
    for znak in tekst:
        nowy+=znak
        nowy+='-'
    return nowy[:-1]


print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))