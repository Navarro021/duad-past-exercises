
with open("input_text.txt", "r", encoding="utf-8") as source_file:
    with open("uppercase_text.txt", "w", encoding="utf-8") as new_file:
        for line in source_file:
            new_file.write(line.upper())

print("Texto en mayúsculas guardado en uppercase_text.txt")
