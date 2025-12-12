import json
with open('dogs.json','r',encoding='utf-8') as file:
    psy=json.load(file)

for pies in psy:
    if pies['age']<5:
        for key,value in pies.items():
            print(key,'::',value)
        print()