
def convertir_a_entero(my_list):
    for value in my_list:
        try:
            number = int(value)
            print(value, "convertido a", number)
        except ValueError:
            print(f"No se pudo convertir el elemento: {value}")


my_list = ['4', 'hola', '10', '5.2']

print("Resultado:")
convertir_a_entero(my_list)
