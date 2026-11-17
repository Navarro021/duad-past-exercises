
import json

with open("pokemon.json", "r", encoding="utf-8") as file:
    pokemons = json.load(file)

for pokemon in pokemons:
    print("Nombre:", pokemon["name"])
    print("Tipo:", pokemon["type"])
    print("Nivel:", pokemon["level"])
    print()
