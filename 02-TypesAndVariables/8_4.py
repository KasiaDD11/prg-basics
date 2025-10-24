cm=int(input('Wzrost w cm: '))
inch=cm*0.394
feet=int(inch//12)
inches=round((inch%12),2)



print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')