"""Escribe un archivo numero_positivo.py que solicite al usuario un número
indique si es positivo, negativo o cero."""
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")