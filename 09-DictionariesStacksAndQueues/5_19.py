'''
The hotel's IT system contains a list of reserved rooms. The data is contained in the reservations.json file. Write a program that prints the summary information as stated below. Break your program into smaller parts defining functions.

number of rooms
number of paid reservations
number of unpaid reservations
total value of paid reservations
total value of unpaid reservations
'''
import json
with open('reservations.json','r',encoding='utf-8') as plik:
    rezerwacje=json.load(plik)
rez=rezerwacje['reservations']
print(len(rez))
un=0
number_un=0
pd=0
number_pd=0
for pokoj in rez:
    if pokoj['paid']==True:
        pd+=1
        number_pd+=pokoj['nights']*pokoj['price_per_night']
    else:
        un+=1
        number_un+=pokoj['nights']*pokoj['price_per_night']

print(f'paid: {pd}, value sum {number_pd}. Unpaid: {un}, value sum {number_un}')
