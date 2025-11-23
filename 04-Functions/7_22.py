
def f(zdanie):
    skrot=''
    if zdanie=='':
        return skrot
    else:
        skrot+=zdanie[0]
        for i in range(len(zdanie)-1):
            if zdanie[i]==' ':
                skrot+=zdanie[i+1]

    return skrot

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))