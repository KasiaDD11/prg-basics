#Write a program that displays the first five lines from the it_company.csv file 
#and then prints 'Press Enter key...' in the next line and waits for the Enter key to be pressed. 
#The program repeats printing the next five lines from the file, waiting for the Enter key to be pressed each time.
    
import re
plik=open('it_company.csv','r')
dane=[]
for linia in plik:
    dane.append(linia.strip())
k=1
for i in range(3):
    print(dane[k])
    
    k+=1

while re.match(input("press enter key"),""):
    for i in range(3):
        print(dane[k])
        k+=1
        