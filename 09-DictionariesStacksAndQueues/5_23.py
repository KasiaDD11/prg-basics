import json
with open('euro.json','r',encoding='utf-8') as file:
    dane=json.load(file)

danee=dane['rates']
print('Date            Buying Rate     Selling Rate')
print('============================================')
for dzien in danee:
    print(f'{dzien["effectiveDate"]}    {dzien["bid"]}      {dzien["ask"]}')