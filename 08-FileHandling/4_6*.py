#file_name = input('wpisz nazwe pliku: ')
file_name='sp.txt'
try:
    with open(file_name) as file:
        content = []
        for linia in file:
            content.append(linia.strip())
except FileNotFoundError:
    print(f"Hey! The file {file_name} does not exist.")

plik=[]
linie=0
char=0
words=0
slowa=[]
for linia in content:
    linie+=1
    lin=linia.split(' ')
    if linia.split(' ')!=['']:
        words+=len(lin)
    
    char+=len(linia)
    
print(linie)
print(char)
print(words)
    
# obliczenia
#linie = content.count("\n") + 1 if content else 0
#chars = len(content.replace("\n", ""))   # znaki BEZ nowych linii
#words = len(content.split())             # słowa

#print("Linie:", linie)
#print("Znaki (bez \\n):", chars)
#print("Słowa:", words)