
words = []
long_words = []

for index in range(5):
    word = input(f"Ingrese la palabra {index + 1}: ")
    words.append(word)

for word in words:
    if len(word) > 4:
        long_words.append(word)

print(long_words)
