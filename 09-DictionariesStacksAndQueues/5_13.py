import queue

dzialanie='8 3 1 + / 3 2 - 4 + * ='
stak=queue.LifoQueue()
for znak in dzialanie:
    if znak in '0123456789':
        stak.put(znak)
    if znak in'+-*/':
        pierwsza=stak.get()
        druga=stak.get()
        if znak=='+':
            stak.put(int(pierwsza)+int(druga))
        elif znak=='*':
            stak.put(int(pierwsza)*int(druga))
        elif znak=='-':
            stak.put(int(druga)-int(pierwsza))
        elif znak=='/':
            stak.put(int(druga)/int(pierwsza))
    if znak=='=':
        print(stak.get())

