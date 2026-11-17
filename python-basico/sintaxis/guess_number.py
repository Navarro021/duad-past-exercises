import random

secret_number = random.randint(1,10)
user_number = 0

while user_number !=secret_number:
	user_number = int(input("adivina el numero del 1 al 10: "))
	
	if user_number == secret_number:
		print("felicidades, adivinaste el numero secreto")
	else:
		print("incorrecto, intenta otra vez.")	