
import csv

with open("videojuegos.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for game in reader:
        print("Nombre:", game[0])
        print("Género:", game[1])
        print("Desarrollador:", game[2])
        print("Clasificación:", game[3])
        print()
