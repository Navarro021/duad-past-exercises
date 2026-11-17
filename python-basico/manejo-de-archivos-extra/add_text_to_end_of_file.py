
new_text = input("Ingrese una línea de texto: ")

with open("records.txt", "a", encoding="utf-8") as file:
    file.write(new_text + "\n")

print("El texto se agregó al final del archivo.")
