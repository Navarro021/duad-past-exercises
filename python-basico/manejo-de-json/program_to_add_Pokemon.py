
import json

# Leer los Pokémon existentes
with open("pokemon.json", "r", encoding="utf-8") as file:
    pokemons = json.load(file)

# Solicitar la información del nuevo Pokémon
name = input("Nombre: ")
pokemon_type = input("Tipo: ")
level = int(input("Nivel: "))
weight = float(input("Peso en kg: "))
shiny_answer = input("¿Es shiny? (si/no): ").lower()
is_shiny = shiny_answer == "si"

held_item = input("Objeto equipado (dejar vacío si no tiene): ")

if held_item == "":
    held_item = None

skills = []

for index in range(4):
    skill = input(f"Habilidad {index + 1}: ")
    skills.append(skill)

stats = {
    "hp": int(input("HP: ")),
    "attack": int(input("Ataque: ")),
    "defense": int(input("Defensa: ")),
    "sp_attack": int(input("Ataque especial: ")),
    "sp_defense": int(input("Defensa especial: ")),
    "speed": int(input("Velocidad: "))
}

new_pokemon = {
    "name": name,
    "type": pokemon_type,
    "level": level,
    "weight_kg": weight,
    "is_shiny": is_shiny,
    "held_item": held_item,
    "skills": skills,
    "stats": stats
}

# Agregar el nuevo Pokémon a la lista
pokemons.append(new_pokemon)

# Guardar la lista actualizada
with open("pokemon.json", "w", encoding="utf-8") as file:
    json.dump(pokemons, file, indent=4, ensure_ascii=False)

print(f"Pokémon {name} agregado correctamente.")
