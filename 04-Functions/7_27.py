def f(code):
    ostatnia=int(code[-1])
    ost=(int(code[1])+int(code[0])+int(code[2]))%7
    if ostatnia==ost:
        return True
    else:
        return False
    

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))