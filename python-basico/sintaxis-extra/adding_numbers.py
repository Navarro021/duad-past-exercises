
number = int(input("Ingrese un número: "))

counter = 1
total = 0

while counter <= number:
    total += counter
    counter += 1

print("El resultado de la suma es:", total)