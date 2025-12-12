import queue
kolejka=queue.Queue()
numer=1

while True:
    obcja=input('Wybierz opcje(1/2/3)\n1 dodaj do kolejki\n2 obsuz kolenego\n3 zakoncz\n\n\n')

    if obcja=='1':
        kolejka.put(numer)
        numer+=1
        print(f'{numer-1} w kolence')
    elif obcja=='2':
        if not kolejka.empty():
            obs=kolejka.get()
            print(f'{obs} obsluzony')
        else:
            print('koniec')
            break

    else:
        break