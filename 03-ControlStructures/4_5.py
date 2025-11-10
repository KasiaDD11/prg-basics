###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for litera in plain_text:
    encrypted_text+=chr(ord(litera)+1)
   

print(plain_text)
print(encrypted_text)