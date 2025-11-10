
dog_age=int(input('wiek psa: '))
if dog_age>2:
    human_age=(dog_age-2)*4+21
else:
    human_age=dog_age*10.5

print(f'Dog that has {dog_age} in human years \nhas {human_age} years in dogs years')