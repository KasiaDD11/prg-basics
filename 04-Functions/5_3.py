
###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import klawiatura as K # your own defined module

# Reads employee's data from keyboard
first_name = K.input_string('Enter name: ')
last_name = K.input_string('Enter last name: ')
age = K.input_integer('Enter your age: ')
salary = K.input_real('Enter your salary: ')
is_salary_hidden = K.input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name: ', first_name)
print('Last name: ',last_name)
print('Age: ',age)
if is_salary_hidden==False:
    print('Salary: ',salary)