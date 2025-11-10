Current_product_price= 140.00
Previous_product_price= 150
discount=(Previous_product_price-Current_product_price)/Previous_product_price*100
if discount>=10:
    print('KUP TEN PRODUKT')
    print(f'{discount}% ZNIŻKI')
else:
    print(f'znika {discount}%')
