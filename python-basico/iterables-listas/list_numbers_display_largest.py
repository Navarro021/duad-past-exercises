numbers = []

for index in range(10):
    number = int(input(f"Ingrese el número {index + 1}: "))
    numbers.append(number)

highest_number = numbers[0]

for number in numbers:
    if number > highest_number:
        highest_number = number

print(f"{numbers}. El más alto fue {highest_number}.")