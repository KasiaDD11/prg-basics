def czy_b(liczba):
    for znak in str(liczba):
        if znak not in ['0','1']:
            return False
        
    return True

print(czy_b("101101"))
print(czy_b("1311a10100"))