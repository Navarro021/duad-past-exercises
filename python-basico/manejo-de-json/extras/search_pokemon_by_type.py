
import json

with open("pokemon.json", "r", encoding="utf-8") as file:
    pokemons = json.load(file)

type_names = {
    "fuego": "fire",
    "agua": "water",
    "electrico": "electric",
    "eléctrico": "electric",
    "planta": "grass"
}

search_type = input("Ingrese el tipo de Pokémon que desea buscar: ").strip().lower()

if search_type in type_names:
    search_type = type_names[search_type]

found = False

print("Los Pokémon que existen de ese tipo son:")

for pokemon in pokemons:
    if pokemon["type"].lower() == search_type:
        print(pokemon["name"])
        found = True

if not found:
    print("No se encontraron Pokémon de ese tipo.")
