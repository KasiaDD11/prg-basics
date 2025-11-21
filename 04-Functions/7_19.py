def f(ciag):
    ciag=str(ciag)
    sum=0
    for liczba in ciag:
        if ciag.count(liczba)>=2:
            sum+=int(liczba)

        
    return sum

print(f(1027) )
print(f(230335)) 
print(f(513553007) )