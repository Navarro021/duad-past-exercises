seconds = int(input("Ingrese el tiempo en segundos: "))

if seconds < 600:
    remaining_seconds = 600 - seconds
    print(remaining_seconds)
elif seconds > 600:
    print("Mayor")
else:
    print("Igual")