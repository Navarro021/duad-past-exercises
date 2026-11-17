total_grades = int(input("Ingrese la cantidad de notas: "))

counter = 1
passed_count = 0
failed_count = 0
passed_sum = 0
failed_sum = 0
total_sum = 0

while counter <= total_grades:
    grade = float(input(f"Ingrese la nota número {counter}: "))

    if grade < 70:
        failed_count += 1
        failed_sum += grade
    else:
        passed_count += 1
        passed_sum += grade

    total_sum += grade
    counter += 1

if total_grades > 0:
    total_average = total_sum / total_grades
else:
    total_average = 0

if passed_count > 0:
    passed_average = passed_sum / passed_count
else:
    passed_average = 0

if failed_count > 0:
    failed_average = failed_sum / failed_count
else:
    failed_average = 0

print("Cantidad de notas aprobadas:", passed_count)
print("Promedio de notas aprobadas:", passed_average)

print("Cantidad de notas desaprobadas:", failed_count)
print("Promedio de notas desaprobadas:", failed_average)

print("Promedio total de notas:", total_average)