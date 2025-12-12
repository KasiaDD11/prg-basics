def avg_speed(distance,hours,minutes):
    average=distance/(hours+minutes/60)
    return round(average,2)
print(avg_speed(70,1,23))