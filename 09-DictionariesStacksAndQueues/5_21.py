import json
ksiazka={
    'tytol':'dwor nocy i costam',
    'autor':'sarah j.mass',
    'rok_wydania': 2016,
    'katekoria':'fantazy',
    'czy_seria':True,
    'bohaterowie':['weira','rysand','tamlin','casian']
}
file_name='favorite.json'
with open(file_name,'w') as file:
    json.dump(ksiazka,file,indent=3)

print('saved')