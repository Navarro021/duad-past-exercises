list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

employee = {}

for index in range(len(list_a)):
    employee[list_a[index]] = list_b[index]

print(employee)