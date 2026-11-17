my_list = []

quantity = int(input("¿Cuántos números desea ingresar? "))

for index in range(quantity):
    number = int(input(f"Ingrese el número {index + 1}: "))
    my_list.append(number)

search_number = int(input("Ingrese el número a buscar: "))
count = 0

for number in my_list:
    if number == search_number:
        count += 1

print(f"El número {search_number} aparece {count} veces")
