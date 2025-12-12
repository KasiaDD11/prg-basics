import queue
stos=queue.LifoQueue()
numer =18
bin=''
while numer>0:
    pomoc=numer%2
    stos.put(pomoc)
    numer=numer//2

while not stos.empty():
    bin+=str(stos.get())

print(bin)
