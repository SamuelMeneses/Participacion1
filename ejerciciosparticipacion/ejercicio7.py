# Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

lista = []
numerosusuario = int(input("Ingrese el numero: "))
lista.append(numerosusuario)
pregunta = input("Va añadir mas numeros? s para si, n para no")

while pregunta == "s" or pregunta == "S":
    numerosusuario= int(input("Añada otro numero "))
    lista.append(numerosusuario)
    pregunta = input("Va añadir mas numeros? s para si, otra tecla para no")

for i in lista:

    maximo = max(lista)
    minimo = min(lista)

print(f"La lista dada {lista}, su numero mayor es {maximo} y su numero menor es {minimo}")