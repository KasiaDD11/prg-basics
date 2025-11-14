def f(number, even):
    suma=0
    if even==True:
        for liczba in str(number):
            if int(liczba)%2==0:
                suma+=int(liczba)


    elif even==False:
         for liczba in str(number):
            if int(liczba)%2==1:
                suma+=int(liczba)
    return suma

print(f(3124,True)) #returns 6
print(f(3124,False)) #returns 4
print(f(20576,False)) #returns 12
print(f(20576,True)) #returns 8
print(f(13115,True)) #returns 0

