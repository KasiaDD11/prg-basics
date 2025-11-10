number=int(input('Wpisz liczbe: '))
def czy_prime(numer):
    for i in range(2,numer):
        if numer%i==0:
            return False
    return True

for i in range(2,number):
    if czy_prime(i):
        print(i)
