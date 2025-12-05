
price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
suma=0
for nazwa,cena in price_list.items():
    print(nazwa,cena)
    suma+=cena
print(round(suma,2))
sum=0
for nazwa,cena in price_list.items():
    cena=round(cena*0.9,2)
    sum+=cena
    print(nazwa,cena)
print(round(sum,2))
