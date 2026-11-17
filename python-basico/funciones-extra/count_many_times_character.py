
def count_character(text, character):
    count = 0

    for letter in text:
        if letter == character:
            count += 1

    return count


text = input("Ingrese un texto: ")
character = input("Ingrese el carácter que desea buscar: ")

result = count_character(text, character)
print(f"Se ha encontrado {result} veces el carácter")
