# Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

import random

def listanumerosaleatorios(h):
    lista = [0] * h
    for i in range(h):
        lista[i] = random.randint(0, 100)

    return lista

h = int(input("Cuantos numeros aleatorios quiere obtener: "))

numerosaleatorios = listanumerosaleatorios(h)

print(numerosaleatorios)
