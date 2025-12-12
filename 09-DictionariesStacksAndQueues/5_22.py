import json
produkt={}
# read product data from keyboard
produkt['nazwa']=str(input('podaj nazwe: '))
produkt['price']=float(input('podaj cene: '))
produkt['paid']=bool(input('Czy zaplacone: (False/True)'))


# save product data to json file
with open('lista.json','w',encoding='utf-8') as file:
    json.dump(produkt,file,indent=2)
    