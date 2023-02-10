# Crear un programa que calcule la suma de los números en una lista dada.

listasuma = []
numerosusuario = int(input("Ingrese el numero: "))
listasuma.append(numerosusuario)
pregunta = input("Va añadir mas numeros? s para si, n para no")
suma = 0
i = 0

while pregunta == "s" or pregunta == "S":
    numerosusuario= int(input("Añada otro numero "))
    listasuma.append(numerosusuario)
    pregunta = input("Va añadir mas numeros? s para si, otra tecla para no")

while i<len(listasuma):
    suma = suma + listasuma[i]
    i = i + 1

print(f"La suma de los elementos de la lista es {suma}")





