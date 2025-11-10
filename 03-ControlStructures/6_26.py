pin='0805'

proba=1
pn=str(input('ENTER THE PIN CODE: '))
while pn!=pin and proba<3:
    print('Incorrect...')
    pn=str(input('ENTER THE PIN CODE: '))
    proba+=1
if pn==pin:
    print('You are logged in')
else:
    print('Sorry, your payment card has been blocked.')

