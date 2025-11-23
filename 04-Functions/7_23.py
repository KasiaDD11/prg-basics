def f(haslo):
    if len(haslo)<6:
        return False
    else:
        for znak in haslo:
            if haslo.count(znak)>1:
                return False
        return True
    

print(f("qwerty"))
print(f(""))
print(f("A2water3"))
print(f("book123"))
print(f("ax15"))