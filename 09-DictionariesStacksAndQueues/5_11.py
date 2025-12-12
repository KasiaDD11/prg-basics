import json
# Read the contents of the json file
plik=open("voting.json","r")
glosy=json.load(plik)
plik.close()

# Vote for a person
person_name = input('Name of the person you are voting for:')
if person_name in glosy:
    glosy[person_name]+=1
else:
    glosy[person_name]=1


# Save voting data to json file
with open("voting.json","w") as file:
    json.dump(glosy,file)