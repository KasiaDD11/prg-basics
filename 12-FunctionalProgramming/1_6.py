avg_speed= lambda distance,hours,minutes:round(distance/(hours+minutes/60),2)
print(avg_speed(70,1,23))