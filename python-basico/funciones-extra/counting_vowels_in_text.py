
def count_vowels(text):
    vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count


text = input("Ingrese un texto: ")
print(count_vowels(text))
