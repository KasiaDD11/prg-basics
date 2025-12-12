basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}
person=basic_data
for data,value in advanced_data.items():
    person[data]=value

print(person)