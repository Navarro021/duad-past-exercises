
import json

with open("pokemon.json", "r", encoding="utf-8") as file:
    pokemons = json.load(file)

levels_by_type = {}

for pokemon in pokemons:
    pokemon_type = pokemon["type"]
    level = pokemon["level"]

    if pokemon_type not in levels_by_type:
        levels_by_type[pokemon_type] = []

    levels_by_type[pokemon_type].append(level)

for pokemon_type in sorted(levels_by_type):
    total = 0

    for level in levels_by_type[pokemon_type]:
        total += level

    average = total / len(levels_by_type[pokemon_type])

    print(f"Tipo: {pokemon_type} → Promedio de nivel: {average:.1f}")
