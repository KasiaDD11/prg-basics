def f(zdanie):
    nowe=""
    for znak in zdanie:
        if znak!=" ":
            nowe+=znak
    return nowe

print(f("integrated development environment")) 
print(f("A programming language is a system of notation for writing computer programs"))