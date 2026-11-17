number = int(input("Ingrese un número del 1 al 10: "))

if number >= 1 and number <= 10:
    for multiplier in range(1, 13):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
else:
    print("El número debe estar entre 1 y 10")