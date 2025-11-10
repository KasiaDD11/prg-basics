car_speed=int(input('Predkosz auta: '))
speed_limit_min=40
speed_limit_max=140

if car_speed<40 or car_speed>140:
    print('WARNING!!!!\nSpeed invalid')
else:
    print('GOOD CAR SPEED')