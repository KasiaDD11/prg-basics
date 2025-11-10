###
# Sums numbers entered by user
#
total_sum = 0
ilosc=0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    ilosc+=1

print(f"The total sum of the numbers is: {total_sum}")
print(f'Srednia z liczb to {total_sum/ilosc}')