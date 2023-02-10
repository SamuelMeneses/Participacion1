# Escribir una función que calcule el área de un círculo dado su radio.

import math

radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * (radio * radio)

print(f"El area del circulo con radio {radio} es {area}")