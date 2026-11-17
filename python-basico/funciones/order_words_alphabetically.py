
def sort_words(text):
    words = text.split("-")
    words.sort()

    return "-".join(words)


print(sort_words("python-variable-funcion-computadora-monitor"))
