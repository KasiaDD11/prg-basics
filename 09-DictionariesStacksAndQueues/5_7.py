hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
suma_kr=0
suma_sop=0
for hotel in hotels_in_Krakow:
    suma_kr+=hotel["price"]
av_kr=suma_kr/len(hotels_in_Krakow)
for hotel in hotels_in_Sopot:
    suma_sop+=hotel["price"]
av_sop=suma_sop/len(hotels_in_Sopot)

if av_kr>av_sop:
    print('W krakowie drozej')
elif av_sop>av_kr:
    print('W sopocie drozej')
else:
    print('tak samo')


print('Krakow')
print(av_kr)
print('Sopot')
print(av_sop)