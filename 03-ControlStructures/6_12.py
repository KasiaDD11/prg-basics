ilosc=5
cena=40

if ilosc>2:
    ile=2*cena+(ilosc-2)*cena*0.75
else:
    ile=ilosc*cena
 



print(f'Number of products purchased: {ilosc}')
print(f'Product price: {cena}')
print(f'Amount to pay: {ile}')