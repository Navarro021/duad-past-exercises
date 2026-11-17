
try:
    name = input("Ingrese su nombre: ")

    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")

except ValueError as error:
    print(error)

else:
    try:
        age = int(input("Ingrese su edad: "))
        print(f"Hola {name}, su edad es {age}")
    except ValueError:
        print("Número no valido")
