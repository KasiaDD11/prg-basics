with open('books.csv','r') as file:
    dane=[]
    for linia in file:
        dane.append(linia.strip().split(','))



print(dane)
for ksiazka in dane:
    if ksiazka[2]=="Fantasy":
        with open('books_fantasy.txt','a') as plik1:
            plik1.write(f'{",".join(ksiazka)}\n')

    elif ksiazka[2]=="Historical":
        with open('books_historical.txt','a') as plik2:
            plik2.write(f'{",".join(ksiazka)}\n')

    elif ksiazka[2]=="Romance":
        with open('books_romance.txt','a') as plik3:
            plik3.write(f'{",".join(ksiazka)}\n')

    elif ksiazka[2]=="Classic":
        with open('books_classic.txt','a') as plik4:
            plik4.write(f'{",".join(ksiazka)}\n')
