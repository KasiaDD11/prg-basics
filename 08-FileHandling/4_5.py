#The file email.txt contains a raw email. 
#Write a program that uses regular expressions t
#o fetch and print:

#sender email address
#ecipient email address
#email subject
#email body

import re
with open("email.txt","r") as file:
    email=file.read()
sender_patern="From.*<([a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+)>"
reci_patern="To.*<([a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+)>"
sub_patern="Subject:\s(.*)"
body_patern="Hi.[\s\S]*Jan Kowalski"
mail=re.findall(sender_patern,email)
print(mail)
mail2=re.findall(reci_patern,email)
print(mail2)
temat=re.findall(sub_patern,email)
print(temat)
body=re.findall(body_patern,email)
cialo=str(body[0])
bo=cialo.replace("\n"," ")
print(bo)

