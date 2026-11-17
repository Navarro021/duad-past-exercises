
def sumar_valores(my_list):
    total = 0

    for value in my_list:
        try:
            number = float(value)
            total += number
            print(number, "sumado correctamente")
        except (ValueError, TypeError):
            print(f"Elemento inválido: {value}")

    print("Total de la suma:", total)


my_list = ['10', 'manzana', '5.5', '3', 'n/a']

sumar_valores(my_list)
