person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

#Displays name
#Displays hobby
#Displays the entire contents of the dictionary
#Changes surname to 'Nowak'
#Changes person's marriage status
#Adds gender: 'male'
#Adds a new hobby: 'bicycle'
#Adds work phone to existing phones: '313131444'
#Displays the entire contents of the dictionary (iterate over dictionary items)
print(person["name"])
print(person["hobby"])

person["surname"]="Nowak"
person["married"]=False
person["gender"]="male"
person["hobby"].append("bicycle")
person["phone"]["work"]="313131444"

for defin,dana in person.items():
    print(f'{defin} : {dana}')