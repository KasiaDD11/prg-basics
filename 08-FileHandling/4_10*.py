import csv
with open('clothing.csv','r',newline='') as plik:
    ubrania=csv.DictReader(plik)
    for linia in ubrania:
        if float(linia['Price'])<60 and float(linia['Stock_Quantity'])<40:
            print(f"{linia['Product_ID']},{linia['Product_Name']}")