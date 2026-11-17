
import csv

genre_counts = {}

with open("videojuegos.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for game in reader:
        genre = game["genero"]

        if genre not in genre_counts:
            genre_counts[genre] = 0

        genre_counts[genre] += 1

print("Géneros encontrados:")

for genre in sorted(genre_counts):
    print(f"{genre}: {genre_counts[genre]}")
