# Crear una función que invierta el orden de los elementos en una lista dada

lista = []
numerosusuario = int(input("Ingrese el numero: "))
lista.append(numerosusuario)
pregunta = input("Va añadir mas numeros? s para si, n para no")

while pregunta == "s" or pregunta == "S":
    numerosusuario= int(input("Añada otro numero "))
    lista.append(numerosusuario)
    pregunta = input("Va añadir mas numeros? s para si, otra tecla para no")

invertir = list(reversed(lista))

print(f"La lista dada {lista} de forma invertida queda {invertir}")

