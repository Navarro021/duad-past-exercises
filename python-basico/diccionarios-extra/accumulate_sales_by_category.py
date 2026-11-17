
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25}
]

result = {}

for product in products:
    category = product["category"]
    price = product["price"]

    if category not in result:
        result[category] = 0

    result[category] += price

print(result)
