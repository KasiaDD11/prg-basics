categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max=expenses[0]
max_i=0
for i in range(len(expenses)):
    if expenses[i]>max:
        max=expenses[i]
        max_i=i
print(max)
print(max_i)
print(categories[max_i])