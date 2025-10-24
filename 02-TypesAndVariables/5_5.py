price=float(input("enter price:"))
dis=float(input("enter discount:"))
after=round((price-price*dis/100),2)
redu=round((price-after),2)
print(f"Enter price: {price} \nAnter discount %: {dis}\nPrice with discount: {after}\nReduction: {redu}")



