###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open('report.txt','r') as file:
   email = file.read()

# regular expression pattern
# for amounts
pattern = '\d{1,4}'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
suma=0
for amount in amounts:
   suma+=int(amount)

# print result
print(suma)