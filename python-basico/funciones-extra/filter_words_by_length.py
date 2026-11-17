
def filter_words(words, minimum_letters):
    result = []

    for word in words:
        if len(word) > minimum_letters:
            result.append(word)

    return result


words = ["cielo", "sol", "maravilloso", "día"]
minimum_letters = int(input("Ingrese el numero de letras minimas en la palabra: "))

print(filter_words(words, minimum_letters))
