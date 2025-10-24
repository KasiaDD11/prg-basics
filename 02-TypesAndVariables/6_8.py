###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = int(ord(first))
last_letter_code=int(ord(last))
number_of_letters = abs(first_letter_code-last_letter_code)-1
print(f'Between {first} and {last} is {number_of_letters} letters')