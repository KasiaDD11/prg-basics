arr=[1,2,3,4,5,6,7,8,9,10]
def ile_wiekszych(liczba,arr):
    ile=0
    for licz in arr:
        if licz>liczba:
            ile+=1

    return ile

print(ile_wiekszych(0,arr))