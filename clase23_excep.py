def evaluaEdad(edad):
	if edad<0:
		raise TypeError("No se perimiten edades menor que 0")

	if edad<20:
		return "Eres muy joven"

	elif edad<40:
		return "Eres joven"

	elif edad<65:
		return "Eres maduro"

	elif edad<100:
		return "Eres de la tercera edad"

print(evaluaEdad(25))




