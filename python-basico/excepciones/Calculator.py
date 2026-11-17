
print("---- Calculadora ----")

current_number = 0

while True:
    print(f"\nNúmero actual: {current_number}")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado")
    print("0. Salir")

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: ingrese una opción numérica válida.")
        continue

    if option == 0:
        print("Calculadora cerrada.")
        break

    elif option == 5:
        current_number = 0
        print("Resultado borrado.")

    elif option >= 1 and option <= 4:
        try:
            new_number = float(input("Ingrese otro número: "))

            if option == 1:
                current_number += new_number
            elif option == 2:
                current_number -= new_number
            elif option == 3:
                current_number *= new_number
            elif option == 4:
                current_number = current_number / new_number

            print(f"Resultado: {current_number}")

        except ValueError:
            print("Error: debe ingresar un número válido.")

        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")

    else:
        print("Error: opción inválida. Seleccione una opción del menú.")
