washing_product = "shoes"
rinse = True
spin = False


###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#

czas= 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')
if program=='j':
    czas+=40
elif program=='u':
    czas+=70
elif program=='s':
    czas+=20
else:
    print('WRONG PROGRAM')

if extra_rinse=='y':
    czas+=15
if extra_spin=='y':
    czas+=9

print(f'Total washing time: {czas} minutes')