

odp1=str(input('SURVEY RESULTS Interested in computer science:(y/n) '))
odp2=str(input('Playing computer games:(y/n) '))
odp3=str(input('Has an Instagram account:(y/n) '))


if odp1=='y':
    ans1='YES'
elif odp1=='n':
    ans1='NO'
else:
    print('zla odp')


if odp2=='y':
    ans2='YES'
elif odp2=='n':
    ans2='NO'
else:
    print('zla odp')


if odp3=='y':
    ans3='YES'
elif odp3=='n':
    ans3='NO'
else:
    print('zla odp')

print(f'SURVEY RESULTS Interested in computer science: {ans1}')
print(f'Playing computer games: {ans2}') 
print(f'Has an Instagram account: {ans3}')