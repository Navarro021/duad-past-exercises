
my_list = [9, 4, 7, 1, 5]

smallest_number = my_list[0]

for number in my_list:
    if number < smallest_number:
        smallest_number = number

print(f"El menor valor es {smallest_number}")
