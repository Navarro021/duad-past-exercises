
import csv

developer = input("Ingrese el nombre del desarrollador: ").strip()
found = False

print(f"Videojuegos desarrollados por {developer}:")

with open("videojuegos.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for game in reader:
        if game["desarrollador"].lower() == developer.lower():
            print(f'- {game["nombre"]} (Clasificación: {game["clasificacion"]}, Género: {game["genero"]})')

            found = True

if not found:
    print("No se encontraron videojuegos de ese desarrollador.")
