arr1=[1,4,8]
arr2=[2,3,4,5,6,7,8,9]
sub=0
for liczba in arr1:
    if liczba not in arr2:
        sub=1
        break

if sub==1:
    print('nie jest subsetem')
else:
    print('jest subsetem')
