
with open("input_text.txt", "r", encoding="utf-8") as file:
    words = []

    for line in file:
        words.append(line.strip())

with open("one_line.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(words))

print("Texto guardado en una sola línea.")
