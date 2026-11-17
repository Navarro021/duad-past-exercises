
import csv

rating = input("Ingrese la clasificación ESRB: ").strip().upper()
found = False

with open("videojuegos.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for game in reader:
        if game["clasificacion"].upper() == rating:
            print("Nombre:", game["nombre"])
            print("Género:", game["genero"])
            print("Desarrollador:", game["desarrollador"])
            print("Clasificación:", game["clasificacion"])
            print()

            found = True

if not found:
    print("No se encontraron videojuegos con esa clasificación.")
