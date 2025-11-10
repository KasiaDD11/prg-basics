###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'
university_expanded = ''

for litera in university:
    university_expanded = university_expanded + litera + ' '

print(university) # original university name
print(university_expanded) # expanded university name