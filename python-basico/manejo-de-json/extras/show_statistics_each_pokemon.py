
import json

with open("pokemon.json", "r", encoding="utf-8") as file:
    pokemons = json.load(file)

for pokemon in pokemons:
    print("Nombre:", pokemon["name"])
    print("Ataque:", pokemon["stats"]["attack"])
    print("Defensa:", pokemon["stats"]["defense"])
    print("Velocidad:", pokemon["stats"]["speed"])
    print()
