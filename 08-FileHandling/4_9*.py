#convenient processing of CSV documents is possible using the CSV module. 
#Find on the Internet how to use this module. Then write a program that,
#based on the it_company.csv file, prints the first name, last name and email 
#(in the given order, without Job Title) of people employed in the position of
#'Graphic Designer'. Sample result:
import csv
with open('it_company.csv','r',newline='') as plik:
    pracownicy=csv.DictReader(plik)

    for linia in pracownicy:
        if linia['Job Title']=='Graphic Designer':
            imie=linia['First Name']
            nazw=linia['Last Name']
            em=linia['Email']
            print(f'{imie} {nazw}, {em}')