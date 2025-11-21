# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food=0
tran=0
uti=0
weeks=[]
for week in monthly_expenses:
    food+=week[0]
    tran+=week[1]
    uti+=week[2]
    weeks.append(week[0]+week[1]+week[2])

total=weeks[0]+weeks[1]+weeks[2]+weeks[3]



# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',tran)
print('Utilities:',uti)
print('Week 1:',weeks[0])
print('Week 2:',weeks[1])
print('Week 3:',weeks[2])
print('Week 4:',weeks[3])
print('---------------')
print('TOTAL:',total)