"""Write a program to translate words from English to Polish. 
The user enters a word in English from the keyboard. 
The program displays the translation of the word or information 
that the translation is unavailable.
"""
translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
slowo=input('Wpisz slowo do pzretlumaczenia: ')
if slowo not in translations:
    print('Translation unavailable')
else:
    print(f'{slowo}: {translations[slowo]}')