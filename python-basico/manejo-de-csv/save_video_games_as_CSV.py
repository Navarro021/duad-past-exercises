
import csv

print("---- Registro de videojuegos (CSV) ----")

quantity = int(input("¿Cuántos videojuegos desea ingresar? "))
games = []

for index in range(quantity):
    print(f"\nVideojuego {index + 1}")

    name = input("Nombre: ")
    genre = input("Género: ")
    developer = input("Desarrollador: ")
    rating = input("Clasificación ESRB: ")

    games.append({
        "nombre": name,
        "genero": genre,
        "desarrollador": developer,
        "clasificacion": rating
    })

headers = ["nombre", "genero", "desarrollador", "clasificacion"]

with open("videojuegos.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(games)

print("Videojuegos guardados en videojuegos.csv")
