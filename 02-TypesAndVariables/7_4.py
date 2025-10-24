import math
cir=int(input('Enter tree circumference in cm:'))
dia=cir/math.pi
czy=dia>=50
print(f'Tree can be cut down:{czy},,{dia}')