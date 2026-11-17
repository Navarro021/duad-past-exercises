
word_count = 0

with open("input_text.txt", "r", encoding="utf-8") as file:
    for line in file:
        words = line.split()
        word_count += len(words)

print("Este archivo contiene", word_count, "palabras")
