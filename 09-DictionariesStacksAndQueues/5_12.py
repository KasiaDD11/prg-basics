import queue
tekst=input("wpisz tekst: ")
text=queue.LifoQueue()
for znak in tekst:
    text.put(znak)
nowy=""
while not text.empty():
    nowy+=str(text.get())

print(tekst)
print(nowy)
