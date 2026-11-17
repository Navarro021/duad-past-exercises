print("Encontrar el número mayor")

first_number = int(input("Ingrese el primer número: "))
second_number = int(input("Ingrese el segundo número: "))
third_number = int(input("Ingrese el tercer número: "))

if first_number >= second_number and first_number >= third_number:
    largest_number = first_number
elif second_number >= first_number and second_number >= third_number:
    largest_number = second_number
else:
    largest_number = third_number

print(f"El número mayor es: {largest_number}")
