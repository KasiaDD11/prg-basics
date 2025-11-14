def time_string(h, m, format):
    godzina=''
    if format=='12':
        if h==0:
            godzina+='12'
        elif h>12:
            h=h-12
        if len(str(h))<2 and h!=0:
            godzina+='0'
            godzina+=str(h)
        elif h!=0:
            godzina+=str(h)
        
        godzina+=':'

        if len(str(m))<2:
            godzina+='0'
            godzina+=str(m)
        else:
            godzina+=str(m)



    elif format=='24':
        if len(str(h))<2:
            godzina+='0'
            godzina+=str(h)
        else:
            godzina+=str(h)
    
        godzina+=':'


        if len(str(m))<2:
            godzina+='0'
            godzina+=str(m)
        else:
            godzina+=str(m)
    return godzina
        
print(time_string(15, 38, '24')) 
print(time_string(8, 3, '24') )
print(time_string(0, 5 ,'24') )
print(time_string(11, 15, '12')) 
print(time_string(0, 7, '12') )
print(time_string(7, 30, '12')) 
print(time_string(12, 46, '12')) 
print(time_string(13, 10, '12')) 
print(time_string(19, 2, '12'))